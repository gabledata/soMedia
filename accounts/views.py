from datetime import datetime
import uuid
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpRequest

from soMedia.utils.event_tracking import get_device_id, send_analytics_payload, get_session_property, is_mobile, get_client

from .forms import ProfileForm, RegistrationForm
from .models import UserProfile

User = get_user_model()


def register(request: HttpRequest):
    """Add a new user"""
    # redirect if user is already loggedIn
    if request.user.is_authenticated:
        return redirect(reverse("chat:home"))
    

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        # Process POSTed Form data
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=request.POST["username"], password=request.POST["password1"]
            )
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            send_analytics_payload({
                "tracks": [{
                    "_type": "register",
                    "_dt": datetime.now(),
                    "_source": "soMedia.web_backend",
                    "_uuid": uuid.uuid4(),
                    "_version": "0.3.0",
                    "device_id": get_device_id(user_profile),
                    "session_id": get_session_property(request, "session_id"),
                    "ip_address": request.get_host(),
                    "path": request.get_full_path(),
                    "is_secure": request.is_secure(),
                    "get_client": get_client(request),
                    "language": "en-us",
                    "account_created": created,
                    "username": user_profile.user.username,
                    "user_website": user_profile.website,
                    "user_bio": user_profile.bio,
                    "user_phone": user_profile.phone,
                    "user_address": user_profile.address,
            }]})

            # authenticate and log user in, then redirect to newsFeeds
            login(request, new_user)
            return redirect(reverse("chat:home"))

    else:
        form = RegistrationForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def profile(request: HttpRequest, username):
    """view profile of user with username"""

    user = User.objects.get(username=username)
    # check if current_user is already following the user
    is_following = request.user.is_following(user)
    user_profile = UserProfile.objects.get(user=user)
    send_analytics_payload({
        "tracks": [{
            "_type": "view_profile",
            "_dt": datetime.now(),
            "_source": "soMedia.web_backend",
            "_uuid": uuid.uuid4(),
            "_version": "0.3.0",
            "device_id": get_device_id(user_profile),
            "session_id": get_session_property(request, "session_id"),
            "ip_address": request.get_host(),
            "path": request.get_full_path(),
            "is_secure": request.is_secure(),
            "is_mobile": is_mobile(request),
            "language": "en-us",
            "username": user_profile.user.username,
            "user_website": user_profile.website,
            "user_bio": user_profile.bio,
            "user_phone": user_profile.phone,
            "user_address": user_profile.address,
        }]})
    
    return render(
        request,
        "accounts/users_profile.html",
        {"user": user, "is_following": is_following},
    )


@login_required
def edit_profile(request: HttpRequest):
    """edit profile of user"""

    if request.method == "POST":
        # instance kwargs passed in sets the user on the modelForm
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        
        if form.is_valid():
            form.save()
            user_profile = UserProfile.objects.get(user=request.user)
            send_analytics_payload({
                "tracks": [{
                    "_type": "edit_profile",
                    "_dt": datetime.now(),
                    "_source": "soMedia.web_backend",
                    "_uuid": uuid.uuid4(),
                    "_version": "0.3.0",
                    "device_id": get_device_id(user_profile),
                    "session_id": get_session_property(request, "session_id"),
                    "ip_address": request.get_host(),
                    "path": request.get_full_path(),
                    "is_secure": request.is_secure(),
                    "is_mobile": is_mobile(request),
                    "language": "en-us",
                    "username": user_profile.user.username,
                    "user_website": user_profile.website,
                    "user_bio": user_profile.bio,
                    "user_phone": user_profile.phone,
                    "user_address": user_profile.address,
            }]})
            return redirect(
                reverse("accounts:view-profile", args=(request.user.username,))
            )
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, "accounts/edit_profile.html", {"form": form})


@login_required
def followers(request: HttpRequest):
    """Return the lists of friends user is  following and not"""

    # get users followed by the current_user
    users_followed = request.user.followers.all()

    # get_users not followed and exclude current_user from the list
    unfollowed_users = User.objects.exclude(id__in=users_followed).exclude(
        id=request.user.id
    )
    user_profile = UserProfile.objects.get(user=request.user)
    send_analytics_payload({
        "tracks": [{
            "_type": "get_followers",
            "_dt": datetime.now(),
            "_source": "soMedia.web_backend",
            "_uuid": uuid.uuid4(),
            "_version": "0.3.0",
            "device_id": get_device_id(user_profile),
            "ip_address": request.get_host(),
            "path": request.get_full_path(),
            "language": "en-us",
            "username": user_profile.user.username,
            "user_website": user_profile.website,
            "user_bio": user_profile.bio,
            "user_phone": user_profile.phone,
            "user_address": user_profile.address,
    }]})
    return render(
        request,
        "accounts/followers.html",
        {"users_followed": users_followed, "unfollowed_users": unfollowed_users},
    )


@login_required
def follow(request: HttpRequest, username):
    """Add user with username to current user's following list"""

    request.user.followers.add(User.objects.get(username=username))
    user_profile = UserProfile.objects.get(user=request.user)
    send_analytics_payload({
        "tracks": [{
            "_type": "follow_user",
            "_dt": datetime.now(),
            "_source": "soMedia.web_backend",
            "_uuid": uuid.uuid4(),
            "_version": "0.3.0",
            "device_id": get_device_id(user_profile),
            "session_id": get_session_property(request, "session_id"),
            "ip_address": request.get_host(),
            "path": request.get_full_path(),
            "is_secure": request.is_secure(),
            "is_mobile": is_mobile(request),
            "language": "en-us",
            "username": user_profile.user.username,
            "user_website": user_profile.website,
            "user_bio": user_profile.bio,
            "user_phone": user_profile.phone,
            "user_address": user_profile.address,
    }]})
    return redirect("accounts:followers")


def unfollow(request: HttpRequest, username):
    """Remove username from user's following list"""

    request.user.followers.remove(User.objects.get(username=username))
    user_profile = UserProfile.objects.get(user=request.user)
    send_analytics_payload({
        "tracks": [{
            "_type": "unfollow_user",
            "_dt": datetime.now(),
            "_source": "soMedia.web_backend",
            "_uuid": uuid.uuid4(),
            "_version": "0.3.0",
            "device_id": get_device_id(user_profile),
            "session_id": get_session_property(request, "session_id"),
            "ip_address": request.get_host(),
            "path": request.get_full_path(),
            "is_secure": request.is_secure(),
            "is_mobile": is_mobile(request),
            "language": "en-us",
            "username": user_profile.user.username,
            "user_website": user_profile.website,
            "user_bio": user_profile.bio,
            "user_phone": user_profile.phone,
            "user_address": user_profile.address,
        }]})
    return redirect("accounts:followers")

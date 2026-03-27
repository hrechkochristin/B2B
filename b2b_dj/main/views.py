from django.shortcuts import render, redirect
from users.models import User
# Create your views here.
def main(request):
    
    if request.method=="POST":
        username=request.POST.get("username")
        
        try:
            user = User.objects.get(username=username)
            request.session["username"] = user.username

            role_path = None

            for field in user._meta.fields:
                if field.name.startswith("is_") and getattr(user, field.name) is True:
                    role_path = field.name.removeprefix("is_")
                    break

            if role_path:
                return redirect(f"/{role_path}s/")

            return render(request, "main/start_page.html", {
                "error": "Для користувача не задано ролі"
            })

        except User.DoesNotExist:
            return render(request, "main/start_page.html", {
                "error": "Користувача не знайдено"
            })
        
    return render(request, "main/start_page.html")
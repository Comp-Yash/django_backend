from core.models import TelegramProfile, User


def link_telegram_user(telegram_username: str,telegram_id: int) -> str:


    user = User.objects.filter(username=telegram_username).first()

    if not user:
        return "You must register on NotifyMe first with the same username."

    profile, created=TelegramProfile.objects.get_or_create(user=user)
    profile.telegram_username=telegram_username
    profile.telegram_user_id=telegram_id
    profile.save()

    return "Your Telegram has been linked successfully!"

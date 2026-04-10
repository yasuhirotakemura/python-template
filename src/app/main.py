from app.config.config import get_settings


def main() -> None:
    app_env = get_settings()

    print(f"App Environment: {app_env}")


if __name__ == "__main__":
    main()

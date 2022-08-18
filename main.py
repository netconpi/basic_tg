
from telegram import Update, Game, InlineQueryResultGame, GameHighScore
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler
from secrets import TOKEN

def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()


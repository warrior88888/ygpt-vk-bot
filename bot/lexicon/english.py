from vkbottle.tools.formatting import Formatter


class Messages:
    welcome_message = Formatter(
        "{header:bold}\n"
        "I'm your personal AI tutor, powered by {brand:bold}. "
        "I'm here to help you master English through real conversation.\n\n"
        "{capabilities_title:underline}\n"
        "• {practice:bold} — Let's talk about anything to break your language barrier.\n"
        "• {tasks:bold} — Need a grammar deep-dive or some vocabulary drills? I've got you.\n"
        "• {essays:bold} — Send me your writing for a professional review and detailed feedback.\n\n"
        "{specialties_title:underline}\n"
        "🌟 {immersion:bold} — Learn natural expressions used by native speakers.\n"
        "🎯 {feedback:bold} — Get instant corrections and clear explanations.\n\n"
        "{commands_title:underline}\n"
        "• {cmd_info:bold} — Show the help message at any time.\n"
        "• {cmd_clear:bold} — Start a fresh conversation and clear our history.\n\n"
        "{footer:italic}"
    ).format(
        header="Welcome to your English Journey! 🇬🇧",
        brand="YandexGPT 5.1 Pro",
        capabilities_title="How we can practice:",
        practice="Fluent Conversations",
        tasks="Grammar & Exercises",
        essays="Writing & Feedback",
        specialties_title="Why practice with me:",
        immersion="Natural Language",
        feedback="Real-time Coaching",
        commands_title="Useful commands:",
        cmd_info="/info",
        cmd_clear="/clear",
        footer="Ready to start? Just send me a message in English! 👇",
    )

    info_message = Formatter(
        "{header:bold}\n"
        "Here's a quick reference for everything you can do.\n\n"
        "{commands_title:underline}\n"
        "• {cmd_info:bold} — Show this help message.\n"
        "• {cmd_clear:bold} — Clear our conversation history and start fresh.\n\n"
        "{usage_title:underline}\n"
        "💬 {chat:bold} — Just type in English and I'll respond, correct, and explain.\n"
        "📝 {essays:bold} — Paste your text and ask for a review.\n"
        "📚 {exercises:bold} — Ask for grammar rules, drills, or vocabulary practice.\n\n"
        "{footer:italic}"
    ).format(
        header="📖 Help & Commands",
        commands_title="Commands:",
        cmd_info="/info",
        cmd_clear="/clear",
        usage_title="How to use me:",
        chat="Free conversation",
        essays="Writing feedback",
        exercises="Grammar & vocabulary",
        footer="Tip: you can ask me anything in plain English — no commands needed! 💡",
    )

    clear_dialog = "✅ Conversation cleared! Let's start fresh — say something to begin a new session. 🚀"
    generating_message = "⏳ Please wait, generating a response..."
    already_processing_message = (
        "⏳ I'm still generating your previous response. Please wait a moment."
    )
    throttle_message = (
        "⏳ You're sending messages too fast. Please wait a moment before trying again."
    )

    error_message = Formatter(
        "{header:bold}\n"
        "I'm sorry, but something went wrong on my side. 🧩\n\n"
        "{details:italic}\n"
        "Even the best tutors need a break sometimes! Please try again in a few moments.\n\n"
        "{footer}"
    ).format(
        header="Oops! A small technical glitch...",
        details="I couldn't process your request or generate a response right now.",
        footer="🔄 Please try sending your message again.",
    )

    no_attachments_message = Formatter(
        "{header:bold}\n"
        "I'm sorry, but I {status:bold} with attachments or files yet. 📎\n\n"
        "{details}\n\n"
        "{footer:italic}"
    ).format(
        header="Wait a moment!",
        status="cannot work",
        details="I am currently focused on text-based conversations to improve your English. However, the ability to analyze files and images is coming very soon!",
        footer="Please send your text directly in the chat for now. 👇",
    )


class Commands:
    clear = "/clear"
    info = "/info"


class EnglishLexicon:
    @classmethod
    def make_welcome_message(cls, name: str | None) -> str:
        if name:
            return f"Hello, {name}! 👋\n" + Messages.welcome_message
        return Messages.welcome_message

    @classmethod
    def make_info_message(cls, name: str | None) -> str:
        if name:
            return f"Hi again, {name}! 👋\n" + Messages.info_message
        return Messages.info_message

    @classmethod
    def make_error_message(cls):
        return Messages.error_message

    @classmethod
    def make_clear_dialog_message(cls):
        return Messages.clear_dialog

    @classmethod
    def make_generating_message(cls):
        return Messages.generating_message

    @classmethod
    def make_already_processing_message(cls):
        return Messages.already_processing_message

    @classmethod
    def make_throttle_message(cls) -> str:
        return Messages.throttle_message

    @classmethod
    def make_no_attachment_message(cls):
        return Messages.no_attachments_message

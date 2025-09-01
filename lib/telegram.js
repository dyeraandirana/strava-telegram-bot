// lib/telegram.js

const TELEGRAM_TOKEN = process.env.TELEGRAM_TOKEN;
const TELEGRAM_API = `https://api.telegram.org/bot${TELEGRAM_TOKEN}`;

export async function sendMessageWithButton(chatId, text, button) {
  const payload = {
    chat_id: chatId,
    text,
    parse_mode: 'Markdown'
  };

  if (button) {
    payload.reply_markup = {
      inline_keyboard: [[{ text: button.text, url: button.url }]]
    };
  }

  await fetch(`${TELEGRAM_API}/sendMessage`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
}

// api/telegram.js

import { sendMessageWithButton } from '../lib/telegram';
import { storeTelegramUser } from '../utils/storage';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).send('Method Not Allowed');
  }

  const body = req.body;

  if (body.message) {
    const chatId = body.message.chat.id;
    const firstName = body.message.from.first_name || 'Teman';
    const text = body.message.text;

    // Simpan ID Telegram user
    await storeTelegramUser(chatId);

    if (text === '/start') {
      const loginUrl = `https://your-vercel-app.vercel.app/api/strava-auth?telegram_id=${chatId}`;
      const message = `👋 Hai ${firstName}! Untuk mulai, silakan login ke Strava dengan tombol di bawah ini:`;

      await sendMessageWithButton(chatId, message, {
        text: '🔗 Login Strava',
        url: loginUrl
      });
    } else {
      await sendMessageWithButton(chatId, `Saya belum paham perintah \"${text}\". Coba ketik /start untuk mulai.`, null);
    }
  }

  res.status(200).send('OK');
}

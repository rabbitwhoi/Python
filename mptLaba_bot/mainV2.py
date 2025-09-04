import asyncio
import sqlite3
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

# ---------------- CONFIG ----------------
BOT_TOKEN = "8485177171:AAHfV9-45tNCv-ngUF5MYTIuppNzZp8V5Q4"
ADMINS = {
    1405345526: "Admin1",
    962513896: "Admin2"
}
DB_PATH = "database.db"

# ---------------- DATABASE ----------------
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        description TEXT,
        file_id TEXT,
        status TEXT DEFAULT 'Новая'
    )
    """)
    conn.commit()
    conn.close()

def add_request(user_id, description, file_id=None):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO requests (user_id, description, file_id) VALUES (?, ?, ?)",
                (user_id, description, file_id))
    conn.commit()
    conn.close()

def get_user_requests(user_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, description, status FROM requests WHERE user_id=?", (user_id,))
    rows = cur.fetchall()
    conn.close()
    return rows

def get_request(req_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM requests WHERE id=?", (req_id,))
    row = cur.fetchone()
    conn.close()
    return row

def update_status(req_id, status):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("UPDATE requests SET status=? WHERE id=?", (status, req_id))
    conn.commit()
    conn.close()

def attach_file(req_id, file_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("UPDATE requests SET file_id=? WHERE id=?", (file_id, req_id))
    conn.commit()
    conn.close()

def get_all_requests():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, user_id, description, status FROM requests")
    rows = cur.fetchall()
    conn.close()
    return rows

# ---------------- FSM ----------------
class RequestForm(StatesGroup):
    waiting_for_description = State()
    waiting_for_file = State()

# ---------------- KEYBOARDS ----------------
def client_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📝 Создать заявку", callback_data="new_request")],
        [InlineKeyboardButton(text="📂 Мои заявки", callback_data="my_requests")],
        [InlineKeyboardButton(text="🆘 Поддержка", callback_data="support")],
        [InlineKeyboardButton(text="🔄 Перезапустить", callback_data="restart")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
    ])

def request_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔄 Перезапустить", callback_data="restart")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back")],
        [InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
    ])

def status_keyboard(req_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Принята", callback_data=f"status_{req_id}_Принята")],
        [InlineKeyboardButton(text="🚧 В работе", callback_data=f"status_{req_id}_В работе")],
        [InlineKeyboardButton(text="🔍 На проверке", callback_data=f"status_{req_id}_На проверке")],
        [InlineKeyboardButton(text="📤 Выполнено", callback_data=f"status_{req_id}_Выполнено")],
        [InlineKeyboardButton(text="❌ Отклонена", callback_data=f"status_{req_id}_Отклонена")]
    ])

# ---------------- BOT ----------------
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

# ---------------- CLIENT ----------------
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("👋 Привет! Я бот для сдачи лабораторных.\n ❗️❗️❗️ Перед началом важно: убедись, что у тебя стоит UserName на аккаунте. ❗️❗️❗️", reply_markup=client_menu())
    

@dp.callback_query(F.data == "restart")
async def restart(call: types.CallbackQuery):
    await call.message.answer("🔄 Перезапуск меню", reply_markup=client_menu())

@dp.callback_query(F.data == "back")
async def back(call: types.CallbackQuery):
    await call.message.answer("🔙 Возврат в главное меню", reply_markup=client_menu())

@dp.callback_query(F.data == "main_menu")
async def main_menu(call: types.CallbackQuery):
    await call.message.answer("🏠 Главное меню:", reply_markup=client_menu())

# ---------- SUPPORT ----------
@dp.callback_query(F.data == "support")
async def support(call: types.CallbackQuery):
    text = "🆘 Поддержка:\n\nЕсли у тебя возникли вопросы, можешь написать администратору:\n\n"
    for admin_id, name in ADMINS.items():
        text += f"👤 {name}: [написать](tg://user?id={admin_id})\n"
    await call.message.answer(text, reply_markup=client_menu(), parse_mode="Markdown")

# ---------- REQUESTS ----------
@dp.callback_query(F.data == "new_request")
async def new_request(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("✍️ Отправь описание задания(ТЗ):", reply_markup=request_menu())
    await state.set_state(RequestForm.waiting_for_description)

@dp.message(RequestForm.waiting_for_description, F.text)
async def process_description(msg: types.Message, state: FSMContext):
    await state.update_data(description=msg.text)
    await msg.answer("📎 Прикрепи файл или напиши 'next':", reply_markup=request_menu())
    await state.set_state(RequestForm.waiting_for_file)

@dp.message(RequestForm.waiting_for_file)
async def process_file(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    description = data.get("description", "(без описания)")

    file_id = None
    if msg.document:
        file_id = msg.document.file_id
    elif msg.text and msg.text.lower() == "next":
        file_id = None

    add_request(msg.from_user.id, description, file_id)
    await state.clear()
    await msg.answer("✅ Заявка создана и отправлена администраторам! В течении 30 мин с вами свяжеться исполнитель!", reply_markup=client_menu())

    for admin_id in ADMINS:
        try:
            username = f"@{msg.from_user.username}" if msg.from_user.username else "❌ без username"

            text = (
            f"📥 Новая заявка!\n"
            f"👤 От: {msg.from_user.full_name}\n"
            f"🆔 ID: {msg.from_user.id}\n"
            f"🔗 Username: {username}\n"
            f"📝 ТЗ: {description}"
            )

            if file_id:
                await msg.bot.send_document(admin_id, file_id, caption=text)
            else:
                await msg.bot.send_message(admin_id, text)
        except Exception as e:
            print(f"Ошибка при отправке админу {admin_id}: {e}")

@dp.callback_query(F.data == "my_requests")
async def my_requests(call: types.CallbackQuery):
    requests = get_user_requests(call.from_user.id)
    if not requests:
        await call.message.answer("У тебя пока нет заявок.", reply_markup=client_menu())
        return
    text = "📂 Твои заявки:\n\n"
    for r in requests:
        desc = r[1] if r[1] else "(без описания)"
        short_desc = desc[:30] + ("..." if len(desc) > 30 else "")
        text += f"#{r[0]} — {short_desc} | Статус: {r[2]}\n"
    await call.message.answer(text, reply_markup=client_menu())

# ---------------- ADMIN CLEAR DB ----------------
@dp.message(Command("clear_requests"))
async def clear_requests(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer("❌ У тебя нет прав для этой команды.")
        return

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DELETE FROM requests;")
    conn.commit()
    conn.close()

    await message.answer("✅ Все заявки успешно удалены из базы данных.")

# ---------------- ADMIN ----------------
@dp.message(Command("admin"))
async def admin_panel(message: types.Message):
    if message.from_user.id not in ADMINS:
        return
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📋 Все заявки", callback_data="all_requests")],
        [InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")]
    ])
    await message.answer("🔧 Панель администратора:", reply_markup=kb)

@dp.callback_query(F.data == "all_requests")
async def all_requests(call: types.CallbackQuery):
    if call.from_user.id not in ADMINS:
        return
    reqs = get_all_requests()
    if not reqs:
        await call.message.answer("Нет заявок.", reply_markup=client_menu())
        return

    kb_buttons = [[InlineKeyboardButton(text=f"#{r[0]} | {r[3]}", callback_data=f"req_{r[0]}")] for r in reqs]
    kb = InlineKeyboardMarkup(inline_keyboard=kb_buttons)
    await call.message.answer("📋 Список заявок:", reply_markup=kb)

@dp.callback_query(F.data.startswith("req_"))
async def request_details(call: types.CallbackQuery):
    if call.from_user.id not in ADMINS:
        return
    req_id = int(call.data.split("_")[1])
    req = get_request(req_id)
    if not req:
        await call.message.answer("❌ Заявка не найдена", reply_markup=client_menu())
        return
    text = f"📌 Заявка #{req[0]}\n👤 Пользователь: {req[1]}\n📝 ТЗ: {req[2]}\n📦 Статус: {req[4]}"
    await call.message.answer(text, reply_markup=status_keyboard(req_id))

@dp.callback_query(F.data.startswith("status_"))
async def change_status(call: types.CallbackQuery):
    if call.from_user.id not in ADMINS:
        return
    _, req_id, status = call.data.split("_", 2)
    req_id = int(req_id)
    update_status(req_id, status)
    req = get_request(req_id)
    await call.message.answer(f"✅ Статус заявки #{req_id} изменен на: {status}", reply_markup=client_menu())
    try:
        await call.bot.send_message(req[1], f"🔔 Статус твоей заявки #{req_id} изменен на: {status}", reply_markup=client_menu())
    except:
        print(f"Не удалось уведомить клиента {req[1]}")

# ---------------- MAIN ----------------
async def main():
    init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

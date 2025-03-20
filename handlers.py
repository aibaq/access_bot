import socket
import subprocess

from aiogram.filters.command import Command
from aiogram import Router

from utils import is_valid_ipv4_address

router = Router()


@router.message(Command("add"))
async def add(message, command):
    ip_address = command.args

    if not is_valid_ipv4_address(ip_address):
        await message.answer(f"Неверный IP-адрес {ip_address}")
    else:
        response = subprocess.run(["ufw-docker", "allow", "from", f"{ip_address}", "proto", "tcp", "to", "any", "port", "80"])
        response1 = subprocess.run(["ufw-docker", "allow", "from", f"{ip_address}", "proto", "tcp", "to", "any", "port", "443"])

        if response.returncode == 0 and response1.returncode == 0:
            await message.answer(f"IP-адрес {ip_address} добавлен в список разрешенных")
        else:
            await message.answer(f"Ошибка добавления IP-адреса {ip_address}")

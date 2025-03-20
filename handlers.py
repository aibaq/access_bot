from aiogram.filters.command import Command
from aiogram import Router
from aiogram.types import ChatMemberAdministrator, ChatMemberOwner, FSInputFile, BufferedInputFile

router = Router()

@router.message(Command("add"))
async def add(message, command):
    ip_address = command.args


@router.message(Command("open_access"))
async def open_access(message, command):
    import main
    member = await main.bot.get_chat_member(message.chat.id, message.from_user.id)
    docker_user_table = iptc.Table(iptc.Table.FILTER)
    chain = iptc.Chain(docker_user_table, "DOCKER-USER")
    reject_ip_addresses = [
        rule for rule in chain.rules if
        rule.out_interface and "br-456bf51da98b" in rule.out_interface and
        rule.target and "REJECT" == rule.target.name
    ]
    try:
        if not isinstance(member, (ChatMemberAdministrator, ChatMemberOwner)):
            raise PermissionDenied
        if not reject_ip_addresses:
            raise IpAddressExistError
        [chain.delete_rule(rule) for rule in reject_ip_addresses]
        await message.answer(f"Доступ на сервер открыт всем")
    except PermissionDenied:
        await message.answer(f"Этот функционал доступен только для администраторов чата")
    except IpAddressExistError:
        await message.answer(f"Доступ на сервер уже открыт, проверьте доступ")


# @router.message(Command("close_access"))
# async def close_access(message, command):

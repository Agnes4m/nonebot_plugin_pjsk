from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot.matcher import Matcher
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata

from .draw import make_ramdom

__version__ = "0.0.2"
__plugin_meta__ = PluginMetadata(
    name="pjsk表情",
    description="pjsk表情包生成,适配nonebot2的插件",
    usage="pjsk 【text】",
    type="application",
    homepage="https://github.com/Agnes4m/nonebot_plugin_pjsk",
    supported_adapters={"~onebot.v11"},
    extra={
        "version": __version__,
        "author": "Agnes4m <Z735803792@163.com>",
    },
)

pjsk = on_command("pjsk", aliases={"啤酒烧烤"}, priority=10)


@pjsk.handle()
async def _(matcher: Matcher, arg: Message = CommandArg()) -> None:
    if text := arg.extract_plain_text():
        await matcher.send(MessageSegment.image(await make_ramdom(text)))

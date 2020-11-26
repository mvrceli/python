from dhooks import Webhook, Embed
import random

hook = Webhook("")

embed = Embed(
    description="",
    color=0x5CDBF0,
    timestamp='now'
)

image1 = ""
image2 = ""

embed.set_author(name='Author Goes Here', icon_url=image1)
embed.add_field(name='Test Field', value='Value of the field')
embed.add_field(name='Another Field', value='Another field')
embed.set_footer(text='Here is footer text', icon_url=image1)

embed.set_thumbnail(image1)
embed.set_image(image2)

hook.send(embed=embed)
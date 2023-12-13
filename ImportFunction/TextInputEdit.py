# ------Discord------
from typing import Any
from discord.ext import commands
from discord import app_commands
from discord.interactions import Interaction
from discord.ui import Modal, TextInput
import discord

class TextInputs(TextInput):
    def __init__(self, mode, label, placeholder, **kwargs):
        max_length = 100
        style = discord.TextStyle.short
        if mode == "Free":
            required = False
        elif mode == "Must":
            required = True
        super().__init__(label=label, placeholder=placeholder, required=required, max_length=max_length, style=style)

    async def callback(self, interaction: discord.Interaction):
        await super().callable(interaction)
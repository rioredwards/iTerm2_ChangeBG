#!/usr/bin/env python3

import iterm2
import os
import random


async def main(connection):
    app = await iterm2.async_get_app(connection)

    async def getRandomImage():
        image_folder = "/Users/rioedwards/Pictures/iterm_bg_photos"

        image_files = [
            f
            for f in os.listdir(image_folder)
            if os.path.isfile(os.path.join(image_folder, f))
        ]

        random_image = os.path.join(image_folder, random.choice(image_files))

        return random_image

    @iterm2.RPC
    async def rand_bg(session_id):
        current_tab = app.get_session_by_id(session_id).tab

        rand_img = await getRandomImage()

        for session in current_tab.sessions:
            profile = await session.async_get_profile()
            await profile.async_set_background_image_location(rand_img)

    await rand_bg.async_register(connection)

    @iterm2.RPC
    async def blend_more(session_id):
        current_tab = app.get_session_by_id(session_id).tab
        for session in current_tab.sessions:
            profile = await session.async_get_profile()
            await profile.async_set_blend(min(1, profile.blend + 0.1))

    await blend_more.async_register(connection)

    @iterm2.RPC
    async def blend_less(session_id):
        current_tab = app.get_session_by_id(session_id).tab
        for session in current_tab.sessions:
            profile = await session.async_get_profile()
            await profile.async_set_blend(max(0, profile.blend - 0.1))

    await blend_less.async_register(connection)

    @iterm2.RPC
    async def transparency_down(session_id):
        print("transparency_down")
        current_tab = app.get_session_by_id(session_id).tab
        for session in current_tab.sessions:
            profile = await session.async_get_profile()
            if profile.transparency == 1:
                # Fully transparent
                await profile.async_set_transparency(0.5)
                await profile.async_set_blur(True)
            elif profile.transparency == 0.5:
                await profile.async_set_transparency(0)
                await profile.async_set_blur(True)
            if profile.transparency == 0:
                # Opaque
                await profile.async_set_use_transparency_initially(False)

    await transparency_down.async_register(connection)

    @iterm2.RPC
    async def transparency_up(session_id):
        print("transparency_up")
        current_tab = app.get_session_by_id(session_id).tab
        for session in current_tab.sessions:
            profile = await session.async_get_profile()
            if profile.transparency == 0:
                # Fully Opaque
                await profile.async_set_transparency(0.5)
                await profile.async_set_blur(True)
            elif profile.transparency == 0.5:
                await profile.async_set_transparency(1)
                await profile.async_set_blur(False)
            if profile.transparency == 1:
                # Fully transparent
                await profile.async_set_use_transparency_initially(True)

    await transparency_up.async_register(connection)


iterm2.run_forever(main)

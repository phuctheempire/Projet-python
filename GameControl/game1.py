import asyncio
import time
from math import inf

from pygame.display import set_mode, flip
from pygame.constants import SCALED
from pygame.event import get

event_handler = ...
drawables = [...]

async def pygame_loop(framerate_limit=inf):
    loop = asyncio.get_event_loop()
    screen_surface = set_mode(size=(480, 255), flags=SCALED, vsync=1)
    next_frame_target = 0.0
    limit_frame_duration = (1.0 / framerate_limit)

    while True:

        if limit_frame_duration:
            # framerate limiter
            this_frame = time.time()
            delay = next_frame_target - this_frame
            if delay > 0:
                await asyncio.sleep(delay)
            next_frame_target = this_frame + limit_frame_duration

        for drawable in drawables:
            drawable.draw(screen_surface)
        events_to_handle = list(get())
        events_handled = loop.create_task(handle_events(events_to_handle))
        await loop.run_in_executor(None, flip)
        # don’t want to accidentally start drawing again until events are done
        await events_handled

async def handle_events(events_to_handle):
    # note that this must be an async def even if it doesn’t await
    for event in events_to_handle:
        event_handler.handle_event(event)

asyncio.run(pygame_loop(120))
# -*- coding: utf-8 -*-
"""
Copyright (C) 2012-2016

This file is part of mason.

mason is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

mason is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with mason.  If not, see <http://www.gnu.org/licenses/>.
"""
import logging

__all__ = ('Rect', 'SDLRect')

logger = logging.getLogger(__file__)

try:
    from pygame import Rect

    SDLRect = Rect
    logger.warn("loaded pygame types")

except ImportError:
    logger.warn("not importing pygame types")

try:
    import sdl

    from mason.rect import Rect

    SDLRect = sdl.Rect
    logger.warn("loaded pysdl2_cffi types")

except ImportError:
    logger.warn("not importing pysdl2_cffi types")

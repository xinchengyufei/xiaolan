# -*- coding: utf-8 -*-

import os
import sys
import json
import wx


sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase

class ScreenDisplay(xiaolanBase):
    
    def __init__(self):

        super(ScreenDisplay, self).__init__()

    def text_display_process(self, title, text, remind, background_image):

        """
        文字展示
        :param title: 标题
        :param text: 文字
        :param remind: 提醒词
        :param background_image: 背景图片
        :return:
        """

    def video_display_process(self, title, url, remind):

        """
        视频播放
        :param url: 视频url
        :param remind: 提醒词
        :param title: 标题
        :return:
        """

    def music_display_process(self, title, url, remind, background_image):

        """
        音乐播放
        :param title: 标题
        :param url: 音乐url
        :param remind: 提醒词
        :param background_image: 背景音乐
        :return:
        """
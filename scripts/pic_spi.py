# coding:utf-8
import os
import threading

import requests
import re
import multiprocessing
from multiprocessing import Pool


class Spider:
    def __init__(self, params):
        self.start_page = params["start_page"]
        self.page_num = params["page_num"]
        self.url = params["url"]
        self.path = params["path"]
        self.dir_name = params["dir_name"]
        self.re = params["re"]
        self.running_flag = params["running"]

    @staticmethod
    def get_response(url):
        response = requests.get(url)
        return response

    def parse_response(self, i):
        res_img = re.compile(self.re)

        current_page = self.get_response(self.url.format(i))
        str_html = current_page.content.decode("utf-8")
        img_list = res_img.findall(str_html)

        if img_list:
            self.start_process(img_list, i)

    def start_process(self, img_list, i):
        try:
            os.chdir(self.path + self.dir_name + "\\")
            os.mkdir(str(i))
        except:
            pass

        os.chdir(self.path + self.dir_name + "\\" + str(i) + "\\")
        print("第{}页".format(i))

        j = 1
        for img in img_list:
            t = threading.Thread(target=self.save_img, args=(img, j,))
            t.start()
            j += 1

    def save_img(self, img, j):
        img_content = self.get_response(img)
        with open("{}.jpg".format(j), "wb") as f:
            f.write(img_content.content if self.running_flag else None)
            # print("----第{}张完成".format(j))

    def run(self):
        try:
            os.chdir(self.path + self.dir_name + "\\")
        except:
            os.chdir(self.path)
            os.mkdir(self.dir_name)
            os.chdir(self.path + self.dir_name + "\\")

        page_list = [p for p in range(self.start_page, self.start_page + self.page_num + 1)]
        # po = Pool(5)
        for page in page_list:
            self.parse_response(page)

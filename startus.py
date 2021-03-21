import itertools
import re
from copy import deepcopy
import pytest
import string


class CreateDictionary:

    def __init__(self):
        pass

    @staticmethod
    def merge_pairs1(key, value):

        pairs = dict()
        for (k, v) in itertools.zip_longest(key, value):
            pairs[k] = v
        pairs = dict(filter(lambda x: x[0] is not None, pairs.items()))

        return pairs

    @staticmethod
    def merge_pairs2(key, values):

        pairs = {k: v for (k, v) in itertools.zip_longest(key, values) if k is not None}

        return pairs

    @staticmethod
    def merge_pairs3(key, values):

        pairs = dict()
        for i, k in enumerate(key):
            if i >= len(values):
                pairs[k] = None
            else:
                pairs[k] = values[i]

        return pairs


class CheckValid:

    def __init__(self, mi=1, mx=20):
        self.min = mi
        self.mx = mx

    @staticmethod
    def check_latin1(txt):
        s1 = txt[0]
        s2 = txt[-1]
        s3 = deepcopy(txt)
        if ('a' <= s1 <= 'z') or ('A' <= s1 <= 'Z'):
            if s2.isalnum():
                txt = re.sub(r'[^a-zA-z0-9-\n.\n]', "", txt)
                if s3 == txt:
                    return True
        return False

    @staticmethod
    def check_latin2(txt):
        txt = txt.lower()
        s1 = txt[0]
        s2 = txt[-1]

        if 'a' <= s1 <= 'z':
            if s2.isalnum():
                txt = txt.replace("-", 'a')
                txt = txt.replace(".", 'a')
                s3 = deepcopy(txt)
                txt = re.sub(r'[^a-z0-9]', "", txt)
                if s3 == txt:
                    return True
        return False

    @staticmethod
    def check_latin3(txt):
        txt = txt.lower()
        char_list_lower = [ch for ch in string.ascii_lowercase]
        char_list_number = [str(i) for i in range(10)]
        valid_char = ['-', '.']
        valid_char += char_list_lower + char_list_number
        s1 = txt[0]
        s2 = txt[-1]

        if s1 in char_list_lower:
            if s2 in char_list_lower or s2 in char_list_number:
                mark = 1

                for ch in txt:
                    if ch not in valid_char:
                        print(ch)
                        mark = 0
                if mark == 1:
                    return True

        return False

    def check_length(self, txt):

        if len(txt) < self.min or len(txt) > self.mx:
            return False
        return True

    def check1(self, txt):

        if CheckValid.check_latin1(txt) and self.check_length(txt):
            return True
        return False

    def check2(self, txt):

        if CheckValid.check_latin2(txt) and self.check_length(txt):
            return True
        return False

    def check3(self, txt):

        if CheckValid.check_latin3(txt) and self.check_length(txt):
            return True
        return False


class ReadLogs:

    def __init__(self, fp='./access.log'):

        self.lis = list()
        with open(fp, 'r') as fl:
            for line in fl:
                self.lis.append(line)

    def top_logs(self, k=10):

        umap = {}
        for item in self.lis:
            ip = item.split("-")[0]
            ip = ip[:-1].strip()
            if ip not in umap:
                umap[ip] = 0
            umap[ip] += 1

        umap = {key: value for key, value in sorted(umap.items(), key=lambda item: item[1])}

        top_ip = []
        for i, key in enumerate(umap):
            if i == k:
                return top_ip
            top_ip.append(key)

        return top_ip

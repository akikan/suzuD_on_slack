#!/usr/bin/env python
# -*- coding: utf-8 -*-

import GenerateText as gt

if __name__ == '__main__':
    # 文書生成
    generator = gt.GenerateText()
    generator.n = 1
    gen_txt = generator.generate().encode('utf-8')

import setuptools

setuptools.setup(
        name = 'werkzeug',
        version = '0.1.0',
        packages = setuptools.find_packages(),
        install_requires=[
                'tqdm',
                'sentencepiece',
                'pyyaml',
            ],
        entry_points = {
            'console_scripts':[
                'progress = werkzeug.progress:main',
                'beta-to-eszett = werkzeug.preproc.beta_to_eszett:main',
                'superspecimeni = werkzeug.preproc.superspecimeni:main',
                'tondi = werkzeug.preproc.tondi:main',
                'renversi = werkzeug.preproc.renversi:main',
                'en-tokenize = werkzeug.preproc.tokenize:en',
                'de-tokenize = werkzeug.preproc.tokenize:de',
                'char-stat = werkzeug.statistik.char:main',
                'sent-stat = werkzeug.statistik.sent:main',
                'compare-vocab = werkzeug.check_fairseq_vocab:main',
                '2yaml = werkzeug.generate.conv_to_yaml:main',
                'yaml2tsv = werkzeug.generate.yaml_to_tsv:main',
                'r2l2tsv = werkzeug.generate.r2l_to_tsv:main',
                'merge-r2l = werkzeug.generate.merge_r2l:main',
                'select-best = werkzeug.generate.select_best:main',
                'fm-grundkiewicz-filter = werkzeug.preproc.grundkiewicz_filter:main',
                'mlm-scoring = werkzeug.mlm.mlm_scoring:main',
                'gec-tag = werkzeug.entag:gec',
                'de-gec-tag = werkzeug.entag:de_gec',
                'en-gec-tag = werkzeug.entag:en_gec',
                'd2e-tag = werkzeug.entag:d2e',
                'e2d-tag = werkzeug.entag:e2d',
                'm22src = werkzeug.m2.m22src:m2_to_src',
                'm22trg = werkzeug.m2.m22trg:m2_to_trg',
                ]},)


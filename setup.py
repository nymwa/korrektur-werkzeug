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
                'char-stat = werkzeug.statistik.char:main',
                'sent-stat = werkzeug.statistik.sent:main',
                'compare-vocab = werkzeug.check_fairseq_vocab:main',
                '2yaml = werkzeug.generate.conv_to_yaml:main',
                'select-best = werkzeug.generate.select_best:main',
                'fm-grundkiewicz-filter = werkzeug.preproc.grundkiewicz_filter:main',
                ]},)


import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

sys.path.insert(0, os.path.join(BASE_DIR, 'scripts'))
sys.path.insert(0, os.path.join(BASE_DIR, 'applications'))


def load_settings(settings, DEBUG=False, **kwargs):
    settings.update(
        {
            'DEBUG': True,

            'ALLOWED_HOSTS': [],

            'ROOT_URLCONF': 'admin.urls',

            'SECRET_KEY': 'r%#^n_u0_%ggm6ezie_(l4%!w@trzbmaho3_0=x^u%b(vj4o5j',

            'WSGI_APPLICATION': 'admin.wsgi.application',

            'INSTALLED_APPS': [
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',

                'xadmin',
                'crispy_forms',
                'reversion',
                'ckeditor',  # 富文本编辑器
                'ckeditor_uploader',  # 富文本编辑器上传图片模块

                'content',
                # 'passport',
                # 'activity',
                'spider',
            ],

            'DATABASES': {
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'HOST': '127.0.0.1',
                    'PORT': 18088,
                    'USER': 'root',
                    'PASSWORD': 'star1022',
                    'NAME': 'ZyAdminDB'
                },
                'windows': {
                    'ENGINE': 'django.db.backends.mysql',
                    'HOST': '127.0.0.1',
                    'PORT': 18088,
                    'USER': 'root',
                    'PASSWORD': 'star1022',
                    'NAME': 'ZyAdminDB'
                },
                'linux': {
                    'ENGINE': 'django.db.backends.mysql',
                    'HOST': '127.0.0.1',
                    'PORT': 3306,
                    'USER': 'admindb',
                    'PASSWORD': 'mysql',
                    'NAME': 'ZyAdminDB'
                },
            },

            'TEMPLATES': [
                {
                    'BACKEND': 'django.template.backends.django.DjangoTemplates',
                    'DIRS': [os.path.join(BASE_DIR, 'templates')],
                    'APP_DIRS': True,
                    'OPTIONS': {
                        'context_processors': [
                            'django.template.context_processors.debug',
                            'django.template.context_processors.request',
                            'django.contrib.auth.context_processors.auth',
                            'django.contrib.messages.context_processors.messages',
                        ],
                    },
                },
            ],

            'MIDDLEWARE': [
                'django.middleware.security.SecurityMiddleware',
                'django.contrib.sessions.middleware.SessionMiddleware',
                'django.middleware.common.CommonMiddleware',
                'django.middleware.csrf.CsrfViewMiddleware',
                'django.contrib.auth.middleware.AuthenticationMiddleware',
                'django.contrib.messages.middleware.MessageMiddleware',
                'django.middleware.clickjacking.XFrameOptionsMiddleware',
            ],

            # Password validation
            'AUTH_PASSWORD_VALIDATORS': [
                {
                    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
                },
                {
                    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
                },
                {
                    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
                },
                {
                    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
                },
            ],

            'LANGUAGE_CODE': 'zh-hans',

            'TIME_ZONE': 'Asia/Shanghai',

            'USE_I18N': True,

            'USE_L10N': True,

            'USE_TZ': False,

            'STATIC_URL': '/static/',

            # 富文本编辑器ckeditor配置
            'CKEDITOR_CONFIGS': {
                'default': {
                    'toolbar': 'full',  # 工具条功能
                    'height': 300,  # 编辑器高度
                    # 'width': 300,  # 编辑器宽
                    # 'skin': 'moono',

                }
            },

            'EDITOR_JQUERY_URL': 'https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js',
            'MEDIA_URL': '/home/klm/PycharmProjects/media/',
            'MEDIA_ROOT': os.path.join(BASE_DIR, '/home/klm/PycharmProjects/media/'),
            'CKEDITOR_UPLOAD_PATH': '/home/klm/PycharmProjects/media/uploads/',

        }
    )


'''
admin/password123456
'''

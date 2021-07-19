# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:\\Users\\Jolo Catacutan\\Documents\\2019 programming files\\PYTHON Game Dev\\Connect4Game-x64 GROUP 3\\_connect4_main_.py'],
             pathex=['C:\\Users\\Jolo Catacutan\\AppData\\Local\\Programs\\Python\\Python38\\Scripts'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='_connect4_main_',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='C:\\Users\\Jolo Catacutan\\Documents\\2019 programming files\\PYTHON Game Dev\\Connect4Game-x64 GROUP 3\\C4.ico')

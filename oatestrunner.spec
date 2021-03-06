# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), 'oatestrunner.py'],
             pathex=['C:\\work\\openadams\\trunk'])
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\oatestrunner', 'oatestrunner.exe'),
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='icons\\appicon.ico')
coll = COLLECT( exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name=os.path.join('dist', 'oatestrunner'))
app = BUNDLE(coll,
             name=os.path.join('dist', 'oatestrunner.app'))

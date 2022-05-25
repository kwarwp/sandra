
{'date': 'Tue May 24 2022 23:52:47.94 GMt-0300 (Hora padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <SyntaxError: Invalid left-hand side in assignment>
'''},
{'date': 'Tue May 24 2022 23:53:08.41 GMt-0300 (Hora padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 3
    elemento.picapau =""
NameError: name 'elemento' is not defined
'''},
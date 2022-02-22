source = "reportline += 1"

reportline = 0

exec(source)

sourceCompiled = compile(source, 'internal variable source', 'exec')
exec(sourceCompiled)

print(reportline)
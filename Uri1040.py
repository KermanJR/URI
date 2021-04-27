N1, N2, N3, N4 = input().split()
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)
Media = ((N1*2) + (N2*3) + (N3*4) + (N4*1))/10
print("Media: {:.1f}".format(Media))
if Media >= 7.0:
	print("Aluno aprovado.")
elif Media < 5.0:
	print("Aluno reprovado.")
elif Media >= 5.0 or Media <= 6.9:
	print("Aluno em exame.")
	Nota_do_exame = float(input())
	print("Nota do exame: {}".format(Nota_do_exame))
	Media2 = (Nota_do_exame + Media )/2
	if Media2 >= 5.0:
		print("Aluno aprovado.")
		print("Media final: {:.1f}".format(Media2))
	elif Media2 <= 4.9:
		print("Aluno reprovado.")
		print("Media final: {:.1f}".format(Media2))


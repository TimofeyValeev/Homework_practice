def angle(a,b,c): #calculating the cosine of the angle opposite the larger side
    maxside=max(a,b,c)
    minside=min(a,b,c)
    middleside=0
    if a>=minside and a<=maxside:
        middleside=a
    if b>=minside and b<=maxside:
        sredstorona=b
    if c>=minside and c<=maxside:
        middleside=c
    cos=(minside+middleside-maxside)/(2*middleside*minside)
    return cos

a=int(input('Введите сторону треугольника: '))
b=int(input('Введите сторону треугольника: '))
c=int(input('Введите сторону треугольника: '))

if a+b>c and a+c>b and c+b>a:
    if a==b and b==c:
        print('Треугольник равносторонний')
    elif a==b or b==c or a==c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник произвольный')

    if angle(a,b,c) > 0:
        print('Треугольник остроугольный')
    elif angle(a,b,c) == 0:
        print('Треугольник прямоугольный')
    else:
        print('Треугольник тупоугольный')
else:
    print('Нельзя построить треугольник')
    

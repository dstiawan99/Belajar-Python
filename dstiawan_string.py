paragraf = '''NolSatu hadir sebagai usAha untuk merespon masalah bersama yaitu banyak lulusan teknologi informatika atau profesional teknologi informatika yang kemampuannya kuranG sementara perusahaan-perusahaan membutuhkan profesional teknologi informatika terbaik dengan kemampuan terkini. 
Selain itu, perkembangan teknologi informatika global Berlangsung sangat cepat dan kemampuan profesional teknologi informatika disarankan selaras dengan perkembangan tersebut.
Profesional teknologi informatika diharapkan dapat membantu perusahaan dalaM mengadopsi teknologi informatika terkini untuk mendOrong proses bisnis perusahaan.
Imbal balik bagi profesional teknologi informatika dari proses ini adalah penghasilan yang cukup dan kesejahteraAN yang baik yang diberikan oleh perusahaaN.
NolSatu adalah media untuk Talenta teknologi informatika dilatih agar memiliki kemampuan terkini kemudian disalurkan ke perusahaan yang membutuhkan.
NolSatu juga media untuk Profesional teknologi informatika dilatih agar kemampuannya termutakhirkan kemudian disalurkan ke perusahaan baru yang membutuhkan.'''

hrfKapital = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S',
              'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
jml = 0
for huruf in paragraf:
    if huruf in hrfKapital:
        jml += 1
print(50*'-=')
print('Banyak Huruf Kapital :', jml, 'huruf')
print(50*'-=')
print('Banyaknya Kalimat : ', len(paragraf.splitlines()), 'kalimat')
print(50*'-=')
print('Banyaknya Kata : ', len(paragraf.split(' ')), 'kata')
print(50*'-=')
kalLow = paragraf.lower()
splitKalLow = kalLow.splitlines()
jmlKata = 0
index = 0
while index < len(splitKalLow):
    if splitKalLow[index].endswith('membutuhkan.'):
        jmlKata+=1
    index += 1
print('banayaknya kalimat yang diawali nolsatu dan di akhiri membutuhkan :',jmlKata,'kalimat')
print(50*'-=')
splitKalimat = paragraf.splitlines()
print(splitKalimat[0].capitalize())
print(splitKalimat[1].capitalize())
print(splitKalimat[2].capitalize())
print(splitKalimat[3].capitalize())
print(splitKalimat[4].capitalize())
print(splitKalimat[5].capitalize())
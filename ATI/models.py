from datetime import datetime
from django.db import models


class Embalagem(models.Model):
    embalagem_id = models.AutoField(primary_key=True, editable=False)
    embalagem_nome = models.TextField(max_length=70, verbose_name="Embalagem")

    def __str__(self):
        return str(self.embalagem_nome)


class Viagem(models.Model):
    viagem_id = models.AutoField(primary_key=True, editable=False)
    viagem_nome = models.TextField(max_length=70, verbose_name="Viagem")
    viagem_atracacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.viagem_nome)


class Pais(models.Model):
    pais_id = models.AutoField(primary_key=True, editable=False)
    pais_nome = models.TextField(max_length=70, verbose_name="Pais")

    def __str__(self):
        return str(self.pais_nome)


class Porto(models.Model):
    porto_id = models.AutoField(primary_key=True, editable=False)
    porto_nome = models.TextField(max_length=70, verbose_name="Porto")

    def __str__(self):
        return str(self.porto_nome)


class NCM(models.Model):
    ncm_id = models.AutoField(primary_key=True, editable=False)
    ncm_nome = models.TextField(max_length=70, verbose_name="NCM")

    def __str__(self):
        return self.ncm_nome


class Faturador(models.Model):
    faturador_id = models.AutoField(primary_key=True, editable=False)
    faturador_nome = models.TextField(max_length=70, verbose_name="Faturador")

    def __str__(self):
        return self.faturador_nome


class Notify(models.Model):
    notify_id = models.AutoField(primary_key=True, editable=False)
    notify_nome = models.TextField(max_length=70, verbose_name="Notify")

    def __str__(self):
        return self.notify_nome


class Representante(models.Model):
    rep_nome = models.CharField(max_length=50, verbose_name="Nome")
    rep_cgc = models.CharField(max_length=14, unique=True, verbose_name="CNPJ/CPF")

    def __str__(self):
        return self.rep_nome


class Importador(models.Model):
    imp_nome = models.CharField(max_length=50, verbose_name="Nome")
    imp_cgc = models.CharField(max_length=14, unique=True, verbose_name="CNPJ/CPF")

    def __str__(self):
        return self.imp_nome


class Comissaria(models.Model):
    com_nome = models.CharField(max_length=50, verbose_name="Nome")
    com_cgc = models.CharField(max_length=14, unique=True, verbose_name="CNPJ/CPF")

    def __str__(self):
        return self.com_nome

class ATI(models.Model):

    DOC_ENTRADA_CHOICES = (
        ("1", "DTC"),
        ("2", "DTA-MARITIMO"),
        ("3", "MIC-DTA"),
        ("4", "DTA-AEREO"),
    )
    TIPO_CHOICES = (
        ("1", "SIM"),
        ("2", "NÃO"),
    )

    ati_id = models.AutoField(primary_key=True)
    ati_merc = models.TextField(default=' ', max_length=70, verbose_name="Mercadoria")
    ati_data_cadastro = models.DateTimeField(auto_now=True)
    ati_doc = models.CharField(default='DTC', max_length=12, choices=DOC_ENTRADA_CHOICES, blank=False, null=False, verbose_name="Doc. Entrada")
    ati_conhec = models.TextField(default=' ', max_length=30, verbose_name="BL")
    ati_qtd = models.IntegerField(default=' ', verbose_name="Quantidade")
    ati_imo = models.CharField(default='2', max_length=3, choices=TIPO_CHOICES, verbose_name="Carga IMO")
    ati_madeira = models.CharField(default='2', max_length=3, choices=TIPO_CHOICES, verbose_name="Carga Madeira")
    ati_temperatura = models.IntegerField(default=' ', verbose_name="Temperatura")
    ati_freetime = models.IntegerField(default=' ', verbose_name="Free Time")
    #CRIAR TABELA PARA ARMADOR?
    ati_armador = models.TextField(default=' ', max_length=30, verbose_name="Armador")
    ati_cif = models.FloatField(default=' ', verbose_name="CIF R$")
    ati_faturador_email = models.EmailField(default=' ', max_length=255, verbose_name="Fatura Taxa DTC")

    #arrumar isso
    viagem_atracacao = models.DateTimeField(default=datetime.now)
    embalagem_id = models.ForeignKey(Embalagem, on_delete=models.PROTECT)
    ncm_id = models.ForeignKey(NCM, on_delete=models.PROTECT)
    viagem_id = models.ForeignKey(Viagem, on_delete=models.PROTECT)
    pais_origem_id = models.ForeignKey(Pais, on_delete=models.PROTECT, related_name="pais_origem")
    pais_procedencia_id = models.ForeignKey(Pais, on_delete=models.PROTECT, related_name="pais_procedencia")
    porto_id = models.ForeignKey(Porto, on_delete=models.PROTECT)
    comissaria_id = models.ForeignKey(Comissaria, on_delete=models.PROTECT)
    importador_id = models.ForeignKey(Importador, on_delete=models.PROTECT)
    representante_id = models.ForeignKey(Representante, on_delete=models.PROTECT)
    notify_id = models.ForeignKey(Notify, on_delete=models.PROTECT)
    faturador_id = models.ForeignKey(Faturador, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.ati_id) + ' / ' + str(self.ati_data_cadastro)[0:4]


class Conteiner(models.Model):
    TIPO_CHOICES = (
        ("1", "SIM"),
        ("2", "NÃO"),
    )
    conteiner_id = models.AutoField(primary_key=True, editable=False)
    conteiner_nome = models.TextField(max_length=70, verbose_name="Conteiner")
    conteiner_lacre = models.TextField(max_length=70, verbose_name="Lacre")
    conteiner_iso = models.TextField(max_length=70, verbose_name="ISO")
    conteiner_imo = models.CharField(default='2', max_length=3, choices=TIPO_CHOICES, verbose_name="IMO")
    ati_id = models.ForeignKey(ATI, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return str(self.conteiner_nome)


class Anexos(models.Model):
    ati_id = models.ForeignKey(ATI, on_delete=models.CASCADE, blank=True, null=True)
    anexo = models.FileField(upload_to='ATI')

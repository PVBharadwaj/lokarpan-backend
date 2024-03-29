from django.db import models
from django.utils import timezone

reportVersionChoices = (

    ('latest', 'latest'),

)




class Report(models.Model):
    reportVersion = models.CharField(choices=reportVersionChoices, blank=False, unique=True, max_length=50,
                                     default='latest')
    FCRAreportFile = models.FileField(blank=False) # FCRA
    LegalreportFile = models.FileField(blank=False) # Section 12A certificate
    PlanningCommisionreportFile = models.FileField(blank=False) # 80 G certificate
    PANcardFile = models.FileField(blank=False, default='default_PAN_card.pdf') # PAN
    MemorandumofAssociation = models.FileField(blank=False, default='default_memo_of_association.pdf') # Memorandum of Association
    CSRcertificationletter = models.FileField(blank=False, default='default_csr_certification.pdf') # CSR certification letter 
    addedDate = models.DateField(
        default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.addedDate.strftime("%Y-%m-%d")

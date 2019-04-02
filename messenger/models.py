from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Menssagem(models.Model):
    autor = models.ForeignKey(User, related_name='autor_messages', on_delete=models.CASCADE, default='Guest')
    content = models.TextField(verbose_name='Conteúdo')
    horario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.autor.username

    def ultimas_15_mensagens():
        return Menssagem.objects.order_by('-horario').all()[:15]

    class Meta:
        verbose_name_plural = "Menssagens"

# -*- coding: utf-8 -*-
import pymorphy2
import nltk
from FullText import FullText

#init
morph = pymorphy2.MorphAnalyzer()

sentence = u"""Грабителя задержали по приметам

         Вчера в отдел полиции №7 «Ленинский» УМВД России по г. Новосибирску поступило заявление от 32-летнего гражданина,
         который сообщил о том, что в минувшее воскресенье около 14.00 на улице Киевской на него напал молодой человек и с
         применением физической силы отобрал золотое кольцо. При этом потерпевший подробно описал, как выглядел преступник.
         Вскоре сотрудники полиции задержали по приметам 20-летнего жителя Ленинского района, ранее судимого за причинение
         тяжкого вреда здоровью. В отношении подозреваемого возбуждено уголовное дело по факту грабежа.
         """

sentence1 = u"""Жители Искитимского района подозреваются в тяжком преступлении

         30 августа в 11.50 в больницу Искитима с тупой травмой живота и ушибом почек доставлен 25-летний житель р.п.Линево.
         В ходе проведения оперативно-разыскных мероприятий сотрудниками полиции установлены подозреваемые в совершении
         преступления – двое местных жителей в возрасте 19 и 16 лет, ранее судимых, которые накануне ночью около магазина
         в р.п.Линево в ходе ссоры, возникшей на почве личных неприязненных отношений, избили потерпевшего. По данному факту проводится проверка."""

NewText = FullText(sentence)
NewText.hl_01()

# tokens = nltk.word_tokenize(sentence)
# for token in tokens:
#     parsed = morph.parse(token)[0]
#     if parsed is None: continue
#
#     #searching for subject
#     if parsed.tag.POS == 'NOUN' and parsed.tag.case == 'nomn':
#         # print(parsed.normal_form)
#         subjects.append(parsed.normal_form)
#     #searching for subject properties
#     if parsed.tag.POS == 'ADJF' and parsed.tag.case == 'nomn':
#         # print(parsed.normal_form)
#         properties.append(parsed.normal_form)
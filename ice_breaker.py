from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
import os

information = """
Cristiano Ronaldo

Article
Talk
Read
View source
View history

Tools
Page extended-confirmed-protected
From Wikipedia, the free encyclopedia
"CR7" redirects here. For other uses, see Cristiano Ronaldo (disambiguation) and CR7 (disambiguation).
In this Portuguese name, the first or maternal family name is dos Santos and the second or paternal family name is Aveiro.
Cristiano Ronaldo
GOIH ComM

Ronaldo with Al-Nassr in 2023
Personal information
Full name	Cristiano Ronaldo dos Santos Aveiro[1]
Date of birth	5 February 1985 (age 40)[2]
Place of birth	Funchal, Madeira, Portugal
Height	1.87 m (6 ft 2 in)[note 1]
Position(s)	Forward
Team information
Current team	Al-Nassr
Number	7
Youth career
1992–1995	Andorinha
1995–1997	Nacional
1997–2002	Sporting CP
Senior career*
Years	Team	Apps	(Gls)
2002–2003	Sporting CP B	2	(0)
2002–2003	Sporting CP	25	(3)
2003–2009	Manchester United	196	(84)
2009–2018	Real Madrid	292	(311)
2018–2021	Juventus	98	(81)
2021–2022	Manchester United	40	(19)
2023–	Al-Nassr	77	(74)
International career‡
2001	Portugal U15	9	(7)
2001–2002	Portugal U17	7	(5)
2003	Portugal U20	5	(1)
2002–2003	Portugal U21	10	(3)
2004	Portugal U23	3	(2)
2003–	Portugal	221	(138)
Medal record
Website	cristianoronaldo.com
Signature
Cristiano Ronaldo signature
* Club domestic league appearances and goals as of 22:40, 26 May 2025 (UTC)
‡ National team caps and goals as of 23:45, 8 June 2025 (UTC)
	
This article is part of
a series about
Cristiano Ronaldo
Portuguese professional footballer
CareerInternational goalsAchievementsRivalry with Lionel Messi
Eponyms and public art
Cristiano Ronaldo International AirportEstádio da MadeiraMuseu CR7
Films
The World at His Feet (2014)Ronaldo (2015)
Family
Kátia AveiroGeorgina Rodríguez
Related
Galaxy CR7
vte
Cristiano Ronaldo dos Santos Aveiro (Portuguese pronunciation: [kɾiʃˈtjɐnu ʁɔˈnaldu] ⓘ; born 5 February 1985) is a Portuguese professional footballer who plays as a forward for and captains both Saudi Pro League club Al-Nassr and the Portugal national team. Nicknamed CR7, he is widely regarded as one of the greatest players in history, and has won numerous individual accolades throughout his career, including five Ballon d'Or awards, a record three UEFA Men's Player of the Year Awards, four European Golden Shoes, and was named five times the world's best player by FIFA.[note 3] He has won 34 trophies in his career, including five UEFA Champions Leagues and the UEFA European Championship. He holds the records for most goals (140) and assists (42) in the Champions League, goals (14) and assists (8) in the European Championship, and most international appearances (221) and international goals (138). He has made over 1,200 professional career appearances, the most by an outfield player, and has scored over 900 official senior career goals for club and country, making him the top goalscorer of all time.

Born in Funchal, Madeira, Ronaldo began his career with Sporting CP before signing with Manchester United in 2003. He became a star player at United, where he won three consecutive Premier League titles, the Champions League, and the FIFA Club World Cup. His 2007–08 season earned him his first Ballon d'Or at age 23. In 2009, Ronaldo became the subject of the then-most expensive transfer in history when he joined Real Madrid in a deal worth €94 million (£80 million). At Madrid, he was at the forefront of the club's resurgence as a dominant European force, helping them win four Champions Leagues between 2014 and 2018, including the long-awaited La Décima. He also won two La Liga titles, including the record-breaking 2011–12 season in which Madrid reached 100 points, and became the club's all-time top goalscorer. He won Ballon d'Ors in 2013, 2014, 2016 and 2017, and was runner-up three times to Lionel Messi, his perceived career rival. Following issues with the club hierarchy, Ronaldo signed for Juventus in 2018 in a transfer worth an initial €100 million, where he was pivotal in winning two Serie A titles. In 2021, he returned to United before joining Al-Nassr in 2023.

Ronaldo made his international debut for Portugal in 2003 at the age of 18 and has earned more than 200 caps, making him history's most-capped male player.[7] He has played in eleven major tournaments. He scored his first international goal in Euro 2004, where he helped Portugal reach the final and subsequently made the team of the tournament. He assumed captaincy of the national team ahead of Euro 2008; and at Euro 2012, he was named in the team of the tournament. Ronaldo led Portugal to their first major tournament title at Euro 2016, being named in the team of the tournament for the third time. In the 2018 World Cup, he had his most prolific World Cup campaign with four goals. He received the Golden Boot as the top scorer of Euro 2020 before playing in his fifth World Cup at the 2022 World Cup. He has won two UEFA Nations Leagues, in 2019 and 2025.

One of the world's most marketable and famous athletes, Ronaldo was ranked the world's highest-paid athlete by Forbes on five occasions, and the world's most famous athlete by ESPN from 2016 to 2019. Time included him on their list of the 100 most influential people in the world in 2014. Ronaldo was named in the UEFA Ultimate Team of the Year in 2015, the All-time UEFA Euro XI in 2016, and the Ballon d'Or Dream Team in 2020. In recognition of his record-breaking goalscoring success, he received special awards for Outstanding Career Achievement by FIFA in 2021 and Champions League All-Time Top Scorer by UEFA in 2024.

Early life
Cristiano Ronaldo dos Santos Aveiro was born on 5 February 1985 in the São Pedro parish of Funchal, the capital of the Portuguese island of Madeira, and grew up in the nearby parish of Santo António.[8][9] He is the fourth and youngest child of Maria Dolores dos Santos Viveiros Aveiro, who worked as a cook in the hospitality industry and a cleaning woman,[10][11] and José Dinis Aveiro, a municipal gardener at the Junta de Freguesia of Santo António and part-time kit man for football club Andorinha.[12][13][14] His great-grandmother on his father's side, Isabel da Piedade, an African woman, was born in the island of São Vicente, in what was then Portuguese Cape Verde, and moved to Madeira Island at 16.[15][16] He has one older brother, Hugo, and two older sisters, Elma and Liliana Cátia "Kátia".[2] He was named after actor and U.S. President Ronald Reagan, whom his father was a fan of.[17] His mother revealed that she wanted to abort him due to poverty, his father's alcoholism, and having too many children already, but her doctor refused to perform the procedure.[18][19] Ronaldo grew up in an impoverished Catholic home, sharing a room with all his siblings.[20]

As a child, Ronaldo played for Andorinha from 1992 to 1995,[21] where his father was the kit man,[12] and later spent two years with Nacional. In 1997, aged 12, he went on a three-day trial with Sporting CP, who signed him for a fee of £1,500.[22] He subsequently moved from Madeira to Lisbon to join Sporting CP's youth system.[22] By age 14, while struggling with his school duties and responsibilities in Escola EB2 de Telheiras, his school in the Telheiras area of Lisbon, Ronaldo believed he had the ability to play semi-professionally and agreed with his mother and his tutor at Sporting CP, Leonel Pontes,[23] to cease his education to focus entirely on football.[24][25] With a troubled life as a student,[26] and although living in Lisbon area away from his Madeiran family,[27][28] he did not complete schooling beyond the 6th grade.[29][30] While popular with other students at school, he had been expelled after throwing a chair at his teacher, who he said had "disrespected" him.[24] One year later, he was diagnosed with tachycardia, a condition that could have forced him to give up playing football.[31] Ronaldo underwent heart surgery where a laser was used to cauterise multiple cardiac pathways into one, altering his resting heart rate.[32] He was discharged from the hospital hours after the procedure and resumed training a few days later.[33] In 2021, Cristiano Ronaldo's mother, Dolores Aveiro, stated in an interview for Sporting CP's official television channel (Sporting TV) that her son would be a bricklayer if he had not become a professional football player.[34]

Growing up, Ronaldo idolised the Brazilian footballers Ronaldinho and Ronaldo Nazário, and has described them as leaving "a beautiful history in football".[35]


"""

if __name__ == "__main__":
    load_dotenv()

    # Defining the template and language/chat model
    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    
    """

    summary_prompt_template = PromptTemplate(
        input_variable=["information"], template=summary_template
    )

    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    llm = ChatOllama(model="llama3")

    # Creating a chain
    # Store the openAI API Key as an environment variable
    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"information": information})

    print(res)

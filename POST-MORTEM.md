# Post-Mortem — Missão de Release:

## Time
- Tech Lead: Nicolas Fernandes Luiz
- Dev A: Maria Eduarda Fernandes Rocha
- Dev B: Igor Vinicius Alves da Sila
- QA/Release: Guilherme Bernardo De Souza

---

## O que funcionou bem:

A divisão de responsabilidades entre os integrantes permitiu que o desenvolvimento ocorresse de forma organizada e paralela. O uso de branches específicas para cada funcionalidade facilitou o controle das alterações e evitou impactos diretos na branch principal. A comunicação entre os membros da equipe também contribuiu para a resolução rápida de dúvidas e para a revisão dos Pull Requests.

## O que deu errado ou foi difícil:

O principal desafio foi a resolução do conflito gerado durante o rebase das branches de desenvolvimento, já que mais de um integrante realizou alterações no mesmo arquivo (utils.py). Foi necessário analisar cuidadosamente as mudanças de cada branch para garantir que nenhuma funcionalidade fosse perdida. Apesar disso, o conflito foi resolvido corretamente sem grandes impactos no cronograma.

## Onde usamos rebase (e por quê):

Utilizamos git rebase develop nas branches feature/dev-a e feature/dev-b antes da abertura dos Pull Requests. O objetivo foi atualizar cada branch com as alterações mais recentes da branch develop, reduzindo a quantidade de commits desnecessários no histórico e facilitando a integração das funcionalidades. O rebase também permitiu identificar e resolver conflitos antes da etapa de revisão dos PRs.


## Onde usamos merge (e por quê):

Utilizamos merge na integração das branches de funcionalidade (feature/dev-a e feature/dev-b) para a branch develop, preservando o histórico de desenvolvimento de cada tarefa. Também realizamos merge da branch release/1.0 para main durante o processo de entrega da versão e, posteriormente, o merge da branch hotfix/fix-filter tanto para main quanto para develop, garantindo que a correção aplicada em produção permanecesse sincronizada com o ambiente de desenvolvimento.

## O que faríamos diferente:

Em uma próxima execução, poderíamos realizar revisões intermediárias com mais frequência para identificar possíveis conflitos mais cedo. Também poderíamos definir padrões de alteração nos arquivos compartilhados para reduzir a chance de conflitos durante os rebases. No geral, o processo ocorreu conforme o planejado e permitiu aplicar boas práticas de versionamento e colaboração utilizando Git e GitHub.

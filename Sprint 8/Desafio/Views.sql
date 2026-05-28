-- Conta a quantidade de filmes lançados em cada década
CREATE OR REPLACE VIEW "vw_qtd_filmes_drama_romance_por_decada" AS 
SELECT
  (FLOOR((anoLancamento / 10)) * 10) decada,
  COUNT(*) qtd_filmes
FROM db_desafiorefined.fato_filmes
WHERE (anoLancamento IS NOT NULL)
GROUP BY (FLOOR((anoLancamento / 10)) * 10)
ORDER BY decada ASC;


-- Conta quantos filmes por década tiveram nota > 8 e mais de 1000 votos
CREATE OR REPLACE VIEW "vw_qtd_filmes_nota10_por_decada" AS 
SELECT
  (FLOOR((f.anoLancamento / 10)) * 10) decada,
  COUNT(*) qtd_filmes
FROM db_desafiorefined.fato_filmes f
WHERE ((f.anoLancamento IS NOT NULL) AND (f.notaMedia > 8) AND (f.numeroVotos > 1000))
GROUP BY (FLOOR((f.anoLancamento / 10)) * 10)
ORDER BY decada ASC;


-- Conta a quantidade de filmes com mais de 100 votos por década
CREATE OR REPLACE VIEW "vw_filmes_com_mais_100_avaliacoes_por_decada" AS 
SELECT
  (FLOOR((anoLancamento / 10)) * 10) decada,
  COUNT(*) qtd_filmes
FROM db_desafiorefined.fato_filmes
WHERE ((numeroVotos > 100) AND (anoLancamento IS NOT NULL))
GROUP BY (FLOOR((anoLancamento / 10)) * 10)
HAVING (COUNT(*) > 100)
ORDER BY qtd_filmes DESC;


-- Calcula a média do número de votos por década
CREATE OR REPLACE VIEW "vw_media_decada_numero_avaliacoes" AS 
SELECT
  (FLOOR((anoLancamento / 10)) * 10) decada,
  CAST(AVG(numeroVotos) AS BIGINT) media_numero_avaliacoes
FROM db_desafiorefined.fato_filmes
WHERE (anoLancamento IS NOT NULL)
GROUP BY (FLOOR((anoLancamento / 10)) * 10)
ORDER BY decada ASC;


-- Calcula a nota média dos filmes por década
CREATE OR REPLACE VIEW "vw_media_decada_nota_avaliacoes" AS 
SELECT
  (FLOOR((anoLancamento / 10)) * 10) decada,
  ROUND(AVG(notaMedia), 1) media_nota_avaliacoes
FROM fato_filmes
WHERE (anoLancamento IS NOT NULL)
GROUP BY (FLOOR((anoLancamento / 10)) * 10)
ORDER BY decada ASC;


-- Seleciona o melhor filme (nota mais alta) em cada década, desempate pelo número de votos
CREATE OR REPLACE VIEW "vw_melhor_filme_por_decada" AS 
SELECT
  decada,
  tituloPrincipal,
  notaMedia,
  numeroVotos
FROM (
   SELECT
     ((anoLancamento / 10) * 10) decada,
     tituloPrincipal,
     notaMedia,
     numeroVotos,
     ROW_NUMBER() OVER (PARTITION BY ((anoLancamento / 10) * 10) ORDER BY notaMedia DESC, numeroVotos DESC) rk
   FROM db_desafiorefined.fato_filmes
   WHERE ((anoLancamento IS NOT NULL) AND (numeroVotos > 1000))
) sub
WHERE (rk = 1)
ORDER BY decada ASC;


-- Seleciona os 5 anos com mais filmes que tiveram pelo menos 100 avaliações
CREATE OR REPLACE VIEW "vw_top5_anos_mais_filmes_100_avaliacoes" AS 
SELECT *
FROM db_desafiorefined.vw_filmes_com_mais_100_avaliacoes
LIMIT 5;


-- Dentro dos top 5 anos mais produtivos, pega o melhor filme (nota mais alta, desempate por votos)
CREATE OR REPLACE VIEW "vw_top1_melhor_filme_top5_anos" AS 
SELECT
  anoLancamento,
  tituloPrincipal,
  notaMedia,
  numeroVotos
FROM (
   SELECT
     f.anoLancamento,
     f.tituloPrincipal,
     f.notaMedia,
     f.numeroVotos,
     ROW_NUMBER() OVER (PARTITION BY f.anoLancamento ORDER BY f.notaMedia DESC, f.numeroVotos DESC) rk
   FROM db_desafiorefined.fato_filmes f
   INNER JOIN db_desafiorefined.vw_top5_anos_mais_filmes_100_avaliacoes t 
     ON (f.anoLancamento = t.anoLancamento)
   WHERE (f.numeroVotos > 1000)
) sub
WHERE (rk = 1)
ORDER BY anoLancamento ASC, notaMedia DESC;


-- Lista os 10 filmes mais populares de 2023 e 2024
CREATE OR REPLACE VIEW "vw_top10_populares_2023_2024" AS 
SELECT
  tituloPrincipal,
  anoLancamento,
  popularidade,
  numeroVotos,
  notaMedia
FROM fato_filmes
WHERE (anoLancamento IN (2023, 2024))
ORDER BY popularidade DESC
LIMIT 10;


-- Lista os 10 filmes mais bem avaliados de 2023 e 2024 (mínimo 1000 votos)
CREATE OR REPLACE VIEW "vw_top10_bem_avaliados_2023_2024" AS 
SELECT
  tituloPrincipal,
  anoLancamento,
  notaMedia,
  numeroVotos
FROM fato_filmes
WHERE ((anoLancamento IN (2023, 2024)) AND (numeroVotos > 1000))
ORDER BY notaMedia DESC, numeroVotos DESC
LIMIT 10;


-- Lista os 10 filmes mais mal avaliados de 2023 e 2024 (mínimo 100 votos)
CREATE OR REPLACE VIEW "vw_top10_mal_avaliados_2023_2024" AS 
SELECT
  tituloPrincipal,
  anoLancamento,
  notaMedia,
  numeroVotos
FROM fato_filmes
WHERE ((anoLancamento IN (2023, 2024)) AND (numeroVotos > 100))
ORDER BY notaMedia ASC, numeroVotos DESC
LIMIT 10;

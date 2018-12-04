library(magrittr)
library(tidyverse)
library(tidygraph)
library(ggraph)

library(dplyr)
library(qdap)
library(networkD3)
library(igraph)
library(stringr) 

ira_data = read.csv("~.csv", header=T, as.is=T, encoding="utf-8")

dim(ira_data)

ira <- ira_data[1:9000,]

g <- ira %>% 
select(userid,retweet_userid) %>%  
  as_tbl_graph()

g

ggraph(g) +
  geom_edge_link() +
  geom_node_point(size = 3, colour = 'steelblue') +
  theme_graph()

g2 <- ira %>% 
  select(userid,retweet_userid) %>%  
  as_tbl_graph(directed = F) %>%  
  activate(nodes) %>% 
  mutate(centrality = centrality_betweenness())

g2

ggraph(g2) +
  geom_edge_link() +
  geom_node_point(aes(size = centrality, colour = centrality)) +
  theme_graph()

#create an edge-list for retweet network
sp = split(ira, ira$is_retweet)
rt = mutate(sp[['TRUE']], sender = substr(text, 5, regexpr(':', text) - 1))
el = as.data.frame(cbind(sender = tolower(rt$), receiver = tolower(rt$screenName)))
el = count(el, sender, receiver) 
el[1:5,] #show the first 5 edges in the edgelist

#centrality
cent <- g %>% 
        mutate(cen = centrality_degree(),
              clo = centrality_closeness(),
              bet = centrality_betweenness(),
              eigen = centrality_eigen(),
              page = centrality_pagerank()) %>% 
        as_tibble %>% 
        arrange(desc(cen))

g %>% with_graph(graph_mean_dist())

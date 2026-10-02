# 📊 Sales Analysis — Python

Projeto de análise exploratória de vendas usando **Python + Pandas + Matplotlib**.

## O que o projeto faz
- Importa dados CSV
- Calcula faturamento por venda
- Agrupa resultados por produto, cidade e mês
- Exibe indicadores básicos no terminal
- Gera gráficos em PNG
- Exporta rankings em CSV

## Estrutura
```text
├── analyze.py
├── data/
│   └── vendas.csv
├── output/
│   └── (arquivos gerados)
└── requirements.txt
```

## Executar
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python analyze.py
```

## Próximas evoluções
Dashboard • tratamento de dados ausentes • testes • conexão com banco de dados • publicação dos resultados.

## 📌 Observações
Os arquivos da pasta `output/` são exemplos de resultados gerados pela análise e podem ser versionados para facilitar a visualização do projeto no GitHub.

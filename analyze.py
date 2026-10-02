from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "vendas.csv"
OUTPUT = ROOT / "output"
OUTPUT.mkdir(exist_ok=True)


def main() -> None:
    df = pd.read_csv(DATA, parse_dates=["data"])
    df["faturamento"] = df["quantidade"] * df["preco_unitario"]
    df["mes"] = df["data"].dt.to_period("M").astype(str)

    por_produto = df.groupby("produto", as_index=False)["faturamento"].sum().sort_values("faturamento", ascending=False)
    por_cidade = df.groupby("cidade", as_index=False)["faturamento"].sum().sort_values("faturamento", ascending=False)
    por_mes = df.groupby("mes", as_index=False)["faturamento"].sum()

    print("=== RESUMO ===")
    print(f"Faturamento total: R$ {df['faturamento'].sum():,.2f}")
    print(f"Unidades vendidas: {df['quantidade'].sum():,}")
    print(f"Ticket médio por pedido: R$ {df['faturamento'].mean():,.2f}")
    print("\n=== FATURAMENTO POR PRODUTO ===")
    print(por_produto.to_string(index=False, formatters={"faturamento": "R$ {:,.2f}".format}))

    plt.figure(figsize=(9, 5))
    plt.bar(por_produto["produto"], por_produto["faturamento"])
    plt.title("Faturamento por produto")
    plt.xlabel("Produto")
    plt.ylabel("Faturamento (R$)")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT / "faturamento_por_produto.png", dpi=150)
    plt.close()

    plt.figure(figsize=(9, 5))
    plt.plot(por_mes["mes"], por_mes["faturamento"], marker="o")
    plt.title("Faturamento por mês")
    plt.xlabel("Mês")
    plt.ylabel("Faturamento (R$)")
    plt.xticks(rotation=25)
    plt.tight_layout()
    plt.savefig(OUTPUT / "faturamento_por_mes.png", dpi=150)
    plt.close()

    por_produto.to_csv(OUTPUT / "ranking_produtos.csv", index=False)
    por_cidade.to_csv(OUTPUT / "ranking_cidades.csv", index=False)
    print(f"\nArquivos gerados em: {OUTPUT}")


if __name__ == "__main__":
    main()

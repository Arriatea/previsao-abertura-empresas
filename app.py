from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st


st.set_page_config(
    page_title="Previsao de Abertura de Empresas - 2026",
    layout="wide",
)

BASE_DIR = Path(__file__).parent
OUTPUTS_DIR = BASE_DIR / "outputs"

AZUL = "#1F6F5B"
AZUL_ESCURO = "#173F3A"
CIANO = "#D6A84F"
CIANO_ESCURO = "#9A6B18"
CINZA_TEXTO = "#27312F"
CINZA_CLARO = "#F7F6F0"
CHART_CONFIG = {
    "displayModeBar": False,
    "responsive": True,
}


st.markdown(
    f"""
    <style>
        .stApp {{
            background: linear-gradient(180deg, #ffffff 0%, {CINZA_CLARO} 100%);
        }}

        [data-testid="stHeader"] {{
            background: rgba(255, 255, 255, 0);
        }}

        #MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"],
        [data-testid="stStatusWidget"], [data-testid="stToolbarActions"],
        [data-testid="stHeaderActionElements"], .stDeployButton, .stAppToolbar,
        a[href*="streamlit.io/cloud"] {{
            display: none !important;
        }}

        .block-container {{
            padding-top: 1.4rem;
            padding-bottom: 2.5rem;
            max-width: 1180px;
        }}

        .case-hero {{
            background: linear-gradient(135deg, {AZUL_ESCURO} 0%, {AZUL} 72%, #6F7A45 100%);
            color: white;
            padding: 34px 38px;
            border-radius: 0 0 18px 18px;
            position: relative;
            overflow: hidden;
            margin-bottom: 26px;
            box-shadow: 0 18px 35px rgba(23, 63, 58, 0.18);
        }}

        .case-hero:before {{
            content: "";
            position: absolute;
            width: 230px;
            height: 230px;
            border-radius: 50%;
            border: 1px solid rgba(255, 255, 255, 0.24);
            background: rgba(214, 168, 79, 0.16);
            right: -82px;
            top: -96px;
        }}

        .brand {{
            font-size: 34px;
            font-weight: 800;
            line-height: 1;
            margin-bottom: 28px;
        }}

        .brand-dot {{
            color: {CIANO};
        }}

        .case-kicker {{
            color: {CIANO};
            font-size: 13px;
            font-weight: 700;
            letter-spacing: .08em;
            text-transform: uppercase;
            margin-bottom: 10px;
        }}

        .case-title {{
            font-size: 42px;
            line-height: 1.08;
            font-weight: 800;
            max-width: 760px;
            margin-bottom: 14px;
        }}

        .case-subtitle {{
            font-size: 17px;
            line-height: 1.45;
            max-width: 730px;
            color: rgba(255, 255, 255, 0.88);
        }}

        .section-title {{
            color: {AZUL};
            font-size: 24px;
            font-weight: 800;
            margin: 18px 0 8px;
        }}

        .section-note {{
            color: {CINZA_TEXTO};
            font-size: 15px;
            margin-bottom: 12px;
        }}

        .kpi-grid {{
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 16px;
            margin: 8px 0 26px;
        }}

        .kpi-card {{
            background: white;
            border: 1px solid #E5E1D4;
            border-left: 6px solid {CIANO};
            border-radius: 14px;
            padding: 18px 18px 14px;
            box-shadow: 0 10px 24px rgba(23, 63, 58, 0.08);
        }}

        .kpi-label {{
            color: {AZUL_ESCURO};
            font-weight: 700;
            font-size: 14px;
            line-height: 1.25;
            margin-bottom: 12px;
            opacity: 0.92;
        }}

        .kpi-value {{
            color: {AZUL};
            font-weight: 800;
            font-size: 38px;
            line-height: 1;
            letter-spacing: 0;
        }}

        div[data-testid="stDataFrame"] {{
            border: 1px solid #E5E1D4;
            border-radius: 14px;
            overflow: hidden;
            box-shadow: 0 10px 24px rgba(23, 63, 58, 0.06);
        }}

        .final-note {{
            background: #FFF8E6;
            border: 1px solid #EAD59A;
            border-left: 6px solid {CIANO};
            color: {AZUL_ESCURO};
            padding: 16px 18px;
            border-radius: 12px;
            margin-top: 16px;
            font-size: 15px;
            line-height: 1.45;
        }}

        .mobile-only {{
            display: none;
        }}

        .mobile-card {{
            background: white;
            border: 1px solid #E5E1D4;
            border-left: 5px solid {CIANO};
            border-radius: 12px;
            padding: 13px 14px;
            margin-bottom: 10px;
            box-shadow: 0 8px 18px rgba(23, 63, 58, 0.07);
        }}

        .mobile-card-title {{
            color: {AZUL};
            font-size: 14px;
            font-weight: 800;
            margin-bottom: 8px;
        }}

        .mobile-card-row {{
            display: flex;
            justify-content: space-between;
            gap: 12px;
            color: {CINZA_TEXTO};
            font-size: 13px;
            line-height: 1.45;
            border-top: 1px solid #EFE8DA;
            padding-top: 7px;
            margin-top: 7px;
        }}

        .mobile-card-row strong {{
            color: {AZUL_ESCURO};
            text-align: right;
            white-space: nowrap;
        }}

        .mobile-card-row.no-border {{
            border-top: 0;
            margin-top: 0;
            padding-top: 0;
        }}

        .chart-wrap {{
            background: white;
            border: 1px solid #E5E1D4;
            border-radius: 14px;
            padding: 8px 8px 2px;
            box-shadow: 0 10px 24px rgba(23, 63, 58, 0.06);
            margin-bottom: 22px;
        }}

        @media (max-width: 700px) {{
            .block-container {{
                padding: 0.7rem 0.8rem 1.5rem;
                max-width: 100%;
            }}

            .case-hero {{
                padding: 20px 17px 22px;
                border-radius: 0 0 18px 18px;
                margin-bottom: 18px;
            }}

            .case-hero:before {{
                width: 140px;
                height: 140px;
                right: -58px;
                top: -56px;
            }}

            .brand {{
                font-size: 24px;
                margin-bottom: 18px;
            }}

            .case-kicker {{
                font-size: 11px;
                margin-bottom: 8px;
            }}

            .case-title {{
                font-size: 25px;
                line-height: 1.12;
                max-width: 92%;
                margin-bottom: 10px;
            }}

            .case-subtitle {{
                font-size: 14px;
                line-height: 1.4;
                max-width: 92%;
            }}

            .section-title {{
                font-size: 20px;
                line-height: 1.2;
                margin: 18px 0 6px;
            }}

            .section-note {{
                font-size: 13px;
                line-height: 1.4;
                margin-bottom: 10px;
            }}

            .kpi-grid {{
                grid-template-columns: 1fr;
                gap: 10px;
                margin: 4px 0 24px;
            }}

            .kpi-card {{
                padding: 16px 16px 15px;
                border-radius: 12px;
            }}

            .kpi-label {{
                color: {AZUL_ESCURO};
                font-size: 13px;
                opacity: 1;
                margin-bottom: 10px;
            }}

            .kpi-value {{
                font-size: 34px;
            }}

            div[data-testid="stDataFrame"] {{
                display: none;
            }}

            .mobile-only {{
                display: block;
            }}

            .chart-wrap {{
                padding: 2px 0 0;
                border-radius: 12px;
                margin-left: -2px;
                margin-right: -2px;
            }}
        }}
    </style>
    """,
    unsafe_allow_html=True,
)


def carregar_csv(nome_arquivo):
    caminho = OUTPUTS_DIR / nome_arquivo
    if not caminho.exists():
        st.error(
            f"Arquivo {nome_arquivo} nao encontrado em outputs/. "
            "Rode o notebook notebooks/modelo_final.ipynb para gerar os CSVs."
        )
        st.stop()
    return pd.read_csv(caminho)


def carregar_csv_opcional(nome_arquivo):
    caminho = OUTPUTS_DIR / nome_arquivo
    if caminho.exists():
        return pd.read_csv(caminho)
    return None


def formatar_numero(valor):
    return f"{valor:,.0f}".replace(",", ".")


def kpi_cards_html(mercado, meta, media):
    return (
        '<div class="kpi-grid">'
        '<div class="kpi-card">'
        '<div class="kpi-label">Mercado projetado em 2026</div>'
        f'<div class="kpi-value">{formatar_numero(mercado)}</div>'
        '</div>'
        '<div class="kpi-card">'
        '<div class="kpi-label">Meta anual para 20% de market share</div>'
        f'<div class="kpi-value">{formatar_numero(meta)}</div>'
        '</div>'
        '<div class="kpi-card">'
        '<div class="kpi-label">Media mensal necessaria</div>'
        f'<div class="kpi-value">{formatar_numero(media)}</div>'
        '</div>'
        '</div>'
    )


def cards_mobile_tabela(tabela, tipo):
    if tipo == "projecao":
        cards = []
        for _, linha in tabela.iterrows():
            cards.append(
                '<div class="mobile-card">'
                f'<div class="mobile-card-title">{linha["mes"]}</div>'
                '<div class="mobile-card-row">'
                '<span>Mercado projetado</span>'
                f'<strong>{formatar_numero(linha["Mercado projetado"])}</strong>'
                '</div>'
                '<div class="mobile-card-row">'
                '<span>Meta 20%</span>'
                f'<strong>{formatar_numero(linha["Meta de vendas 20%"])}</strong>'
                '</div>'
                '</div>'
            )
        return '<div class="mobile-only">' + "".join(cards) + "</div>"

    if tipo == "incerteza":
        cards = []
        for _, linha in tabela.iterrows():
            cards.append(
                '<div class="mobile-card">'
                '<div class="mobile-card-row no-border">'
                f'<span>{linha["Indicador"]}</span>'
                f'<strong>{formatar_numero(linha["Valor"])}</strong>'
                '</div>'
                '</div>'
            )
        return '<div class="mobile-only">' + "".join(cards) + "</div>"

    return ""


historico_mensal = carregar_csv("historico_mensal.csv")
previsao_2026_mensal = carregar_csv("previsao_2026_mensal.csv")
tabela_market_share = carregar_csv("tabela_market_share.csv")
resumo_market_share = carregar_csv("resumo_market_share.csv")
resumo_incerteza = carregar_csv_opcional("resumo_incerteza.csv")

historico_mensal["data"] = pd.to_datetime(historico_mensal["data"])
previsao_2026_mensal["data"] = pd.to_datetime(previsao_2026_mensal["data"])
tabela_market_share["data"] = pd.to_datetime(tabela_market_share["data"])

resumo = dict(zip(resumo_market_share["indicador"], resumo_market_share["valor"]))

mercado_total = resumo.get(
    "Mercado projetado em 2026",
    previsao_2026_mensal["previsao_aberturas"].sum(),
)
meta_anual = resumo.get(
    "Meta anual para 20% de market share",
    tabela_market_share["meta_vendas_20_market_share"].sum(),
)
media_mensal = resumo.get(
    "Media mensal de vendas necessarias",
    tabela_market_share["meta_vendas_20_market_share"].mean(),
)
media_mensal = resumo.get("Média mensal de vendas necessárias", media_mensal)

st.markdown(
    """
    <section class="case-hero">
        <div class="brand">Forecast Analytics<span class="brand-dot">.</span></div>
        <div class="case-kicker">Case tecnico anonimizado</div>
        <div class="case-title">Previsao de abertura de empresas em 2026</div>
        <div class="case-subtitle">
            Painel para apresentar a estimativa de mercado e a meta de vendas
            necessaria para buscar 20% de market share, com dados e identidade
            da organizacao analisada anonimizados para portfolio.
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    kpi_cards_html(mercado_total, meta_anual, media_mensal),
    unsafe_allow_html=True,
)

st.markdown('<div class="section-title">Historico mensal + projecao 2026</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-note">Visao do mercado historico junto com a curva prevista para 2026.</div>',
    unsafe_allow_html=True,
)

fig_historico = go.Figure()
fig_historico.add_trace(
    go.Scatter(
        x=historico_mensal["data"],
        y=historico_mensal["abertura_empresas"],
        mode="lines",
        name="Historico",
        line=dict(color=AZUL, width=3, shape="spline"),
        hovertemplate="Historico: %{y:,.0f}<extra></extra>",
    )
)
fig_historico.add_trace(
    go.Scatter(
        x=previsao_2026_mensal["data"],
        y=previsao_2026_mensal["previsao_aberturas"],
        mode="lines+markers",
        name="Projecao 2026",
        line=dict(color=CIANO_ESCURO, width=4),
        marker=dict(size=8, color=CIANO),
        hovertemplate="Projecao: %{y:,.0f}<extra></extra>",
    )
)
fig_historico.update_layout(
    xaxis_title="",
    yaxis_title="Empresas",
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="left",
        x=0,
    ),
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(color=CINZA_TEXTO, size=13),
    margin=dict(l=8, r=8, t=34, b=10),
    hovermode="x unified",
    height=330,
)
fig_historico.update_xaxes(
    showgrid=True,
    gridcolor="#EFE8DA",
    tickformat="%Y",
    tickfont=dict(color=AZUL_ESCURO, size=12),
)
fig_historico.update_yaxes(
    showgrid=True,
    gridcolor="#EFE8DA",
    tickfont=dict(color=AZUL_ESCURO, size=12),
)
st.markdown('<div class="chart-wrap">', unsafe_allow_html=True)
st.plotly_chart(fig_historico, width="stretch", config=CHART_CONFIG)
st.markdown('</div>', unsafe_allow_html=True)

if {"limite_inferior", "limite_superior"}.issubset(previsao_2026_mensal.columns):
    st.markdown('<div class="section-title">Projecao 2026 com faixa de incerteza</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-note">A faixa de incerteza foi criada com base no erro percentual observado na validacao de 2025. Ela nao representa um intervalo de confianca estatistico formal, mas uma margem operacional para apoiar o planejamento.</div>',
        unsafe_allow_html=True,
    )

    fig_incerteza = go.Figure()

    fig_incerteza.add_trace(
        go.Scatter(
            x=previsao_2026_mensal["data"],
            y=previsao_2026_mensal["limite_superior"],
            mode="lines",
            line=dict(width=0),
            showlegend=False,
            hovertemplate="Limite superior: %{y:,.0f}<extra></extra>",
        )
    )

    fig_incerteza.add_trace(
        go.Scatter(
            x=previsao_2026_mensal["data"],
            y=previsao_2026_mensal["limite_inferior"],
            mode="lines",
            fill="tonexty",
            name="Faixa de incerteza",
            fillcolor="rgba(214, 168, 79, 0.22)",
            line=dict(width=0),
            hovertemplate="Limite inferior: %{y:,.0f}<extra></extra>",
        )
    )

    fig_incerteza.add_trace(
        go.Scatter(
            x=previsao_2026_mensal["data"],
            y=previsao_2026_mensal["previsao_aberturas"],
            mode="lines+markers",
            name="Projecao central",
            line=dict(color=AZUL, width=3),
            marker=dict(size=7, color=CIANO),
            hovertemplate="Projecao central: %{y:,.0f}<extra></extra>",
        )
    )

    fig_incerteza.update_layout(
        xaxis_title="",
        yaxis_title="Empresas",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0,
        ),
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color=CINZA_TEXTO, size=13),
        margin=dict(l=8, r=8, t=34, b=10),
        hovermode="x unified",
        height=320,
    )
    fig_incerteza.update_xaxes(
        showgrid=True,
        gridcolor="#EFE8DA",
        tickformat="%b",
        tickfont=dict(color=AZUL_ESCURO, size=12),
    )
    fig_incerteza.update_yaxes(
        showgrid=True,
        gridcolor="#EFE8DA",
        tickfont=dict(color=AZUL_ESCURO, size=12),
    )
    st.markdown('<div class="chart-wrap">', unsafe_allow_html=True)
    st.plotly_chart(fig_incerteza, width="stretch", config=CHART_CONFIG)
    st.markdown('</div>', unsafe_allow_html=True)

    if resumo_incerteza is not None:
        resumo_incerteza_app = resumo_incerteza.rename(
            columns={
                "indicador": "Indicador",
                "valor": "Valor",
            }
        )

        st.dataframe(
            resumo_incerteza_app,
            width="stretch",
            hide_index=True,
        )
        st.markdown(
            cards_mobile_tabela(resumo_incerteza_app, "incerteza"),
            unsafe_allow_html=True,
        )

st.markdown('<div class="section-title">Meta mensal de vendas</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-note">Distribuicao mensal da meta estimada para atingir 20% de market share.</div>',
    unsafe_allow_html=True,
)

fig_meta = go.Figure()
meses_curto = [
    "Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
    "Jul", "Ago", "Set", "Out", "Nov", "Dez"
]
fig_meta.add_trace(
    go.Bar(
        x=meses_curto[:len(tabela_market_share)],
        y=tabela_market_share["meta_vendas_20_market_share"],
        name="Meta mensal",
        marker_color=CIANO,
        marker_line_color=CIANO_ESCURO,
        marker_line_width=1,
        hovertemplate="Meta: %{y:,.0f}<extra></extra>",
    )
)
fig_meta.add_hline(
    y=media_mensal,
    line_dash="dash",
    line_color=AZUL,
    annotation_text=f"Media mensal: {formatar_numero(media_mensal)}",
    annotation_font_color=AZUL,
)
fig_meta.update_layout(
    xaxis_title="",
    yaxis_title="Vendas",
    showlegend=False,
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(color=CINZA_TEXTO, size=13),
    margin=dict(l=8, r=8, t=20, b=10),
    height=320,
)
fig_meta.update_xaxes(showgrid=False, tickfont=dict(color=AZUL_ESCURO, size=12))
fig_meta.update_yaxes(
    showgrid=True,
    gridcolor="#EFE8DA",
    tickfont=dict(color=AZUL_ESCURO, size=12),
)
st.markdown('<div class="chart-wrap">', unsafe_allow_html=True)
st.plotly_chart(fig_meta, width="stretch", config=CHART_CONFIG)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">Projecao mensal de 2026</div>', unsafe_allow_html=True)

tabela_app = tabela_market_share.copy()
tabela_app["mes"] = tabela_app["data"].dt.strftime("%m/%Y")
tabela_app = tabela_app.rename(
    columns={
        "mercado_projetado": "Mercado projetado",
        "meta_vendas_20_market_share": "Meta de vendas 20%",
    }
)
tabela_app = tabela_app[["mes", "Mercado projetado", "Meta de vendas 20%"]]

st.dataframe(
    tabela_app,
    width="stretch",
    hide_index=True,
)
st.markdown(
    cards_mobile_tabela(tabela_app, "projecao"),
    unsafe_allow_html=True,
)

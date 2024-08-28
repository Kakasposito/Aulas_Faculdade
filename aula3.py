{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO4Aymb5vJKWTX7/kE1SgV/",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Kakasposito/Aulas_Faculdade/blob/master/aula3.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Solicita as duas notas do aluno\n",
        "nota1 = float(input(\"Digite a primeira nota: \"))\n",
        "nota2 = float(input(\"Digite a segunda nota: \"))\n",
        "\n",
        "# Calcula a média das notas\n",
        "media = (nota1 + nota2) / 2\n",
        "\n",
        "# Exibe a média\n",
        "print(f\"Sua média foi: {media:.2f}\")\n",
        "\n",
        "# Verifica se o aluno está aprovado ou reprovado\n",
        "if media >= 7:\n",
        "    print(\"Aprovado\")\n",
        "else:\n",
        "    print(\"Reprovado\")\n"
      ],
      "metadata": {
        "id": "JeX7Pnav94qu"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Solicita as notas do aluno\n",
        "nota1 = float(input(\"Digite a primeira nota: \"))\n",
        "nota2 = float(input(\"Digite a segunda nota: \"))\n",
        "\n",
        "# Calcula a média das notas\n",
        "media = (nota1 + nota2) / 2\n",
        "\n",
        "# Solicita a quantidade de atestados e faltas\n",
        "atestados = int(input(\"Digite a quantidade de atestados: \"))\n",
        "faltas = int(input(\"Digite a quantidade de faltas: \"))\n",
        "\n",
        "# Verifica se o aluno está reprovado por faltas\n",
        "if faltas >= 6:\n",
        "    status = \"Reprovado por faltas\"\n",
        "else:\n",
        "    # Verifica se a média é suficiente para aprovação\n",
        "    if media >= 7:\n",
        "        status = \"Aprovado\"\n",
        "    else:\n",
        "        status = \"Reprovado com nota vermelha\"\n",
        "\n",
        "# Exibe os resultados\n",
        "print(f\"Média: {media:.2f}\")\n",
        "print(f\"Status final: {status}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_DEo1uBtV6A1",
        "outputId": "b6aab7fb-8c2b-4d7f-8faa-3aeb973bc5c6"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a primeira nota: 7\n",
            "Digite a segunda nota: 7\n",
            "Digite a quantidade de atestados: 0\n",
            "Digite a quantidade de faltas: 6\n",
            "Média: 7.00\n",
            "Status final: Reprovado por faltas\n"
          ]
        }
      ]
    }
  ]
}
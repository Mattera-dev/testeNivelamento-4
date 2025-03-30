<template>
  <div class="search-container">
    <input
      type="text"
      v-model="search"
      @input="debouncedSearch"
      placeholder="Write your search..."
      class="search-input"
    />
    <div class="buttons">
      <button class="button back" @click="decrementPage" :disabled="page == 0">←</button>
      <p class="page-info">
        {{ page + 1 }}
      </p>
      <button class="button next" @click="incrementPage" :disabled="lastPage">→</button>
    </div>

    <ul class="results-list" v-if="results.length >= 1">
      <li class="result" v-for="(result, index) in results" :key="index">
        <div class="info">
          <p class="title">Razão Social:</p>
          <p class="data">{{ result.razaoSocial }}</p>
        </div>

        <div class="info">
          <p class="title">Nome Fantasia:</p>
          <p class="data">{{ result.nomeFantasia || 'Não informado' }}</p>
        </div>

        <div class="info">
          <p class="title">CNPJ:</p>
          <p class="data">{{ result.cnpj }}</p>
        </div>

        <div class="info">
          <p class="title">Modalidade:</p>
          <p class="data">{{ result.modalidade }}</p>
        </div>

        <div class="info">
          <p class="title">Endereço:</p>
          <p class="data">{{ result.rua }}, {{ result.numero }} {{ result.complemento || '' }}</p>
        </div>

        <div class="info">
          <p class="title">Bairro:</p>
          <p class="data">{{ result.bairro }}</p>
        </div>

        <div class="info">
          <p class="title">Cidade:</p>
          <p class="data">{{ result.cidade }}</p>
        </div>

        <div class="info">
          <p class="title">UF:</p>
          <p class="data">{{ result.uf }}</p>
        </div>

        <div class="info">
          <p class="title">CEP:</p>
          <p class="data">{{ result.cep }}</p>
        </div>

        <div class="info">
          <p class="title">Telefone:</p>
          <p class="data">{{ result.tel || 'Não informado' }}</p>
        </div>

        <div class="info">
          <p class="title">Email:</p>
          <p class="data">{{ result.email || 'Não informado' }}</p>
        </div>

        <div class="info">
          <p class="title">Representante:</p>
          <p class="data">{{ result.representante }}</p>
        </div>

        <div class="info">
          <p class="title">Cargo do Representante:</p>
          <p class="data">{{ result.cargoRepresentante }}</p>
        </div>

        <div class="info">
          <p class="title">Região:</p>
          <p class="data">{{ result.regiao || 'Não informado' }}</p>
        </div>

        <div class="info">
          <p class="title">Data de Registro:</p>
          <p class="data">{{ formatData(result.dataRegistro) }}</p>
        </div>
      </li>
    </ul>

    <p v-else class="no-results">Not found results!</p>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { debounce } from 'lodash'

interface Result {
  idOperadora: string
  cnpj: string
  razaoSocial: string
  nomeFantasia: string | null
  modalidade: string
  rua: string
  numero: string
  complemento: string | null
  bairro: string
  cidade: string
  uf: string
  cep: string
  ddd: string | null
  tel: string | null
  fax: string | null
  email: string | null
  representante: string
  cargoRepresentante: string
  regiao: string | null
  dataRegistro: string
  msg: string | null
}

export default defineComponent({
  name: 'SearchPage',
  async setup() {
    const search = ref<string>('')
    const results = ref<Result[]>([])
    const page = ref<number>(0)
    const lastPage = ref<boolean>(false)

    const searchFunc = async () => {
      try {
        const response = await fetch(
          `http://127.0.0.1:5000/search?s=${search.value}&page=${page.value}`,
        )
        const data = await response.json()
        lastPage.value = false
        if (data.length == 0 || data.length < 20) lastPage.value = true
        results.value = data
      } catch (error) {
        console.error('Error in fetch:', error)
      }
    }

    const decrementPage = async () => {
      page.value = page.value - 1
      await searchFunc()
    }

    const incrementPage = async () => {
      page.value = page.value + 1
      await searchFunc()
    }

    const formatData = (data: string) => {
      const dateTime = new Date(data)
      return dateTime.toLocaleString('pt-br')
    }

    const debouncedSearch = debounce(async () => {
      page.value = 0
      await searchFunc()
    }, 300)

    await searchFunc()
    return {
      search,
      page,
      debouncedSearch,
      decrementPage,
      formatData,
      incrementPage,
      lastPage,
      results,
    }
  },
})
</script>
<style scoped>
.search-container {
  width: 97%;
  margin: 40px auto;
  padding: 30px;
  text-align: center;
  background-color: var(--color-background-soft2);
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.search-input {
  width: 100%;
  padding: 12px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 16px;
  outline: none;
  transition: all 0.3s ease;
}

.search-input:focus {
  border-color: #4caf50;
}

.buttons {
  display: flex;
  width: 100%;
  justify-content: center;
  align-items: center;
}

.buttons .page-info {
  width: 5%;
  border: white 1px solid;
}

.results-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.result {
  display: flex;
  min-height: 300px;
  flex-direction: row;
  flex-wrap: wrap;
  background-color: #fff;
  padding: 20px;
  margin-bottom: 10px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgb(255, 255, 255);
}

.result .info {
  width: 20%;
  height: 50%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.result p {
  margin: 5px 0;
  font-size: 14px;
  color: #333;
}

.result .title {
  font-weight: bold;
  color: #333;
}

.result .data {
  font-size: 14px;
  text-align: start;
  color: #666;
}

.result .data span {
  color: #333;
  font-weight: 600;
}

.no-results {
  font-size: 16px;
  color: #888;
  margin-top: 20px;
}

.button {
  font-size: 48px;
  color: white;
  background: none;
  border: none;
  cursor: pointer;
  margin: 0 10%;
  transition: 0.5s;
}

.button:disabled {
  color: grey;
  cursor: not-allowed;
}

.button:disabled:hover {
  text-shadow: none;
}

.button:hover {
  text-shadow: #575757 3px 4px 0px;
}

@media screen and (max-width: 1480px) {
  .result {
    min-height: 400px;
  }

  .result .info {
    width: 33%;
  }
}

@media screen and (max-width: 1480px) {
  .result {
    min-height: 400px;
  }

  .result .info {
    width: 33.3%;
  }
}

@media screen and (max-width: 900px) {
  .result {
    min-height: 600px;
  }

  .result .info {
    width: 50%;
  }
}
@media screen and (max-width: 640px) {
  .result {
    min-height: 600px;
  }

  .result .info {
    width: 100%;
  }
}
</style>

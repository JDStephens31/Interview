class DataFetcher {
    constructor() {
        this.apiUrl = "https://jsonplaceholder.typicode.com/users";
    }

    async fetchData() {
        const response = await fetch(this.apiUrl);
        const data = await response.json();
    }

    async displayData() {
        const data = await this.fetchData();
        console.log("Fetched Data: ", data);
    }
}

// Main Program
const fetcher = new DataFetcher();
fetcher.displayData();

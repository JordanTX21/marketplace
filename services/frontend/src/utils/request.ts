import axios from 'axios';

export default class Request {

    domain:string;
    prefix:string;

    constructor(){
        this.domain = import.meta.env.VITE_SERVICES_DOMAIN
        this.prefix = 'api'
    }

    async get(endpoint:string,data:any=null){
        try{
            const response = await axios.get(`${this.domain}/${this.prefix}/${endpoint}`,{
                params: {...data}
            })
            return response.data
        }catch(e){
            return {success:false,message:'Ocurrió un error interno.',error: e}
        }
    }

    async post(endpoint:string,data?:any){
        try{
            const response = await axios.post(`${this.domain}/${this.prefix}/${endpoint}`,data)///${this.prefix}
            return response.data
        }catch(e){
            return {success:false,message:'Ocurrió un error interno.',error: e}
        }
    }

    async put(endpoint:string,data?:any){
        try{
            const response = await axios.put(`${this.domain}/${this.prefix}/${endpoint}`,data)
            return response.data
        }catch(e){
            return {success:false,message:'Ocurrió un error interno.',error: e}
        }
    }

    async delete(endpoint:string){
        try{
            const response = await axios.delete(`${this.domain}/${this.prefix}/${endpoint}`)
            return response.data
        }catch(e){
            return {success:false,message:'Ocurrió un error interno.',error: e}
        }
    }
}
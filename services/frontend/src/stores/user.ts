interface UserData {
    id: number;
    name: string;
    email: string;
    password: string;
    photo: string | null;
    rol: string;
    description: string | null;
    created_at: string;
    updated_at: string | null;
    status: boolean;
}
class UserSingleton {
    private static instance: UserSingleton;

    // Propiedades de ejemplo
    private data: UserData | null = null;

    // Constructor privado para evitar instanciación externa
    private constructor() { }

    // Método estático para acceder a la instancia única
    public static getInstance(): UserSingleton {
        if (!UserSingleton.instance) {
            UserSingleton.instance = new UserSingleton();
        }
        return UserSingleton.instance;
    }

    public setData(data: UserData): void {
        this.data = data;
        localStorage.setItem('user_data', JSON.stringify(this.data));
    }

    // Método de ejemplo
    public getData(): UserData | null {
        const data = JSON.parse(localStorage.getItem('user_data') || '');
        if(data) this.data = data
        return this.data;
    }
}

export default UserSingleton;

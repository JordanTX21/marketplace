import { defineStore } from 'pinia';
import { useForm } from 'vee-validate';
import * as Yup from 'yup';

const searchSchema = Yup.object({
    email: Yup.string().email().required(),
    password: Yup.string().min(6).required(),
});

export const useSearchStore = defineStore('search', () => {
    const { errors, defineField, handleSubmit } = useForm({
        validationSchema: searchSchema,
    });
    const [search, searchProps] = defineField('search');

    const sendSearch = handleSubmit((values: {}) => {
        // send values to API
        console.log('Submit', JSON.stringify(values, null, 2));
    });

    const clearSearch = () => {
        search.value = ""
    }
    return {
        errors,
        search,
        searchProps,
        sendSearch,
        clearSearch
    }
})
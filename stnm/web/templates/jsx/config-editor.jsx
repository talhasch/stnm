const ConfigEditor = () => {

    const [params, setParams] = useState([]);

    useEffect(() => {
        fetch("/api/config-params").then(r => r.json()).then((r) => {
            setParams(r);
        })
    }, []);

    console.log(params)

    return (<span>Config editor</span>)
};
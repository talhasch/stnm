const ConfigEditor = ({onSuccess}) => {
    const {object, fetchConfig} = React.useContext(ConfigContext);

    const [params, setParams] = useState([]);
    const [param, setParam] = useState("");
    const [value, setValue] = useState("");
    const [changed, setChanged] = useState(false);
    const [inProgress, setInProgress] = useState(false);

    useEffect(() => {
        fetch("/api/config-params").then(r => r.json()).then((r) => {
            setParams(r);
            paramChanged(r[0]);
        })
    }, []);

    const paramChanged = (param) => {
        setParam(param);
        const [section, key] = param.split(".");

        let value = "";
        if (object[section] !== undefined && object[section][key] !== undefined) {
            value = String(object[section][key]);
        }

        setValue(value);
        setChanged(false);
    }

    const save = () => {
        setInProgress(true);
        const data = {"input": `${param}=${value}`};

        fetch("/api/config", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }).then(r => {
            return r.json();
        }).then(r => {
            if (r.success) {
                toastr.success(r.message, "Done!");

                fetchConfig().then(() => {
                    onSuccess();
                });
            }

            if (r.error) {
                toastr.error(r.message, "Error!");
                setInProgress(false);
            }
        }).catch(() => {
            toastr.error("Unknown error", "Error!");
            setInProgress(false);
        })
    }

    return <Fragment>
        <Row>
            <Col sm="5">
                <FormControl value={param} as="select" disabled={inProgress} onChange={(e) => {
                    paramChanged(e.target.value);
                }}>
                    {params.map(x => <option value={x} key={x}>{x}</option>)}
                </FormControl>
            </Col>
            <Col sm="5">
                <FormControl type="text" disabled={inProgress} value={value} onChange={(e) => {
                    const {value} = e.target;
                    setValue(value);
                    setChanged(true);
                }}/>
            </Col>
            <Col sm="2">
                <Button onClick={save} disabled={!changed || inProgress}>Save {inProgress && <span>...</span>}</Button>
            </Col>
        </Row>
    </Fragment>
};
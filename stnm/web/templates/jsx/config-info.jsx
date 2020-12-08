const ConfigInfo = () => {
    const {loading, raw} = React.useContext(ConfigContext);
    const {status} = React.useContext(NodeContext);

    if (loading === null || !status) {
        return null;
    }

    const [edit, setEdit] = useState(false);

    return <Fragment>
        <div className="card config-info">
            <h5 className="card-header">Config</h5>
            <div className="card-body">
                {raw !== null && (<pre className="config-pre">
            {raw}
            </pre>)}
            </div>
            <div className="card-footer text-muted">
                <Button
                    onClick={() => {
                        setEdit(true);
                    }}
                    type="primary" size="sm">Edit</Button>
            </div>
        </div>

        {edit && (
            <Modal show={true} size="lg" centered={true} animation={false} backdrop="static" keyboard={false} onHide={() => {
                setEdit(false);
            }}>
                <Modal.Header closeButton>
                    <Modal.Title>Edit Config</Modal.Title>
                </Modal.Header>
                <Modal.Body><ConfigEditor onSuccess={() => {
                    setEdit(false);
                }}/></Modal.Body>
            </Modal>
        )}
    </Fragment>
};
const ConfigInfo = () => {
    const {loading, raw} = React.useContext(ConfigContext);
    const {status} = React.useContext(NodeContext);

    if (loading === null || !status) {
        return null;
    }

    const {Modal} = ReactBootstrap;


    return <div className="card config-info">
        <h5 className="card-header">Config</h5>
        <div className="card-body">
            {raw !== null && (<pre className="config-pre">
            {raw}
            </pre>)}
        </div>

        {/*

        <Modal show={true} onHide={() => {

        }}>
            <Modal.Header closeButton>
                <Modal.Title>Modal heading</Modal.Title>
            </Modal.Header>
            <Modal.Body>Woohoo, you're reading this text in a modal!</Modal.Body>
            <Modal.Footer>

            </Modal.Footer>
        </Modal>
    */}
    </div>
};